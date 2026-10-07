"""Reproduce RUNTIME's small proof-checking demo with Lean 4.34.1.

python3 run.py --lean /path/to/lean
The negative controls must fail. This does not verify OpenAI's research proofs.
"""
import argparse,hashlib,json,subprocess,tempfile
from pathlib import Path
from model import checks

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--lean',default='lean');args=p.parse_args()
    base=Path(__file__).resolve().parent
    version=subprocess.check_output([args.lean,'--version'],text=True).strip()
    if 'version 4.34.1,' not in version:raise SystemExit('Use the recorded Lean version 4.34.1 for this reproduction.')
    rows=[]
    for name,exit_code in [('Good.lean',0),('Broken.lean',1),('False.lean',1),('Admitted.lean',0)]:
        f=base/(name+'.txt')
        # Plain-text source is copied without modification to its Lean filename.
        with tempfile.TemporaryDirectory(prefix='runtime-proof-') as tmp:
            (Path(tmp)/name).write_bytes(f.read_bytes())
            r=subprocess.run([args.lean,name],cwd=tmp,text=True,capture_output=True,timeout=60)
        out=r.stdout+r.stderr
        assert r.returncode==exit_code,(name,r.returncode,out)
        if name=='Good.lean':assert 'does not depend on any axioms' in out and 'sorryAx' not in out
        if name=='Admitted.lean':assert 'sorryAx' in out and 'warning:' in out
        rows.append(dict(file=name,sha256=hashlib.sha256(f.read_bytes()).hexdigest(),exit_code=r.returncode,output=out))
        print(name,'expected result confirmed',flush=True)
    result={'lean_version':version,'scope':'Original educational examples, not research theorem reproduction.','runs':rows,'polynomial':checks()}
    (base/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print('All four expected outcomes and exact arithmetic checks reproduced.')

if __name__=='__main__':main()

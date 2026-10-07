# How do you check an AI proof?

Original RUNTIME teaching examples accompanying the OpenAI math explainer.
Watch: [OpenAI Released 722 Math Papers. How Do We Check Them?](https://youtu.be/7wwZYNm4JBc)

This companion is not an independent
verification of OpenAI's research results, and it contains no model weights.

## Run the experiment

Requirements: Python 3.10+ and [Lean 4.34.1](https://github.com/leanprover/lean4/releases/tag/v4.34.1).
Choose the Lean release for your OS/CPU and extract it. On Linux, the .tar.zst
release requires a zstd-capable tar. You do not need Mathlib, a GPU, API access,
or a paid account for these examples. Download this repository using GitHub's
Code > Download ZIP button and extract it, or clone it:

```sh
git clone https://github.com/Runtime-weekly/ai-proof-checking.git
cd ai-proof-checking
```

Run from the downloaded companion folder:

```sh
python3 run.py --lean /absolute/path/to/lean-4.34.1/bin/lean
```

Use the actual binary path in your downloaded distribution. If Lean is already
on PATH at version 4.34.1, `python3 run.py` is sufficient.

| File | Expected result | What it shows |
|---|---|---|
| Good.lean | exit 0, no axiom dependencies | a+b is a valid witness |
| Broken.lean | exit 1, type mismatch | changing the witness to a breaks the proof |
| False.lean | exit 1 | decide rejects 2=3 |
| Admitted.lean | exit 0 with warning and sorryAx | success status alone is insufficient |

The four source examples are stored as `*.lean.txt` plain-text files. The runner
copies their exact bytes into temporary `*.lean` files before invoking Lean,
then removes those temporary files. To open one directly in a Lean editor,
copy it to the same filename without the final `.txt`.

The script asserts these outcomes and saves `results.json`. The original
Spark run is included separately as `recorded-results.json`. Negative controls
are deliberately invalid and must not be used as accepted proof artifacts.

`model.py` calculates n²+n+41 by exact arithmetic. Forty initial values are prime;
at n=40 the value is 1681=41². This illustrates the gap between checking examples
and proving a universal statement. The checker demonstration instead proves
that 2a+2b=2(a+b), for natural a and b, using a+b as its existential witness.

## Research sources and limits

The revised video also plots four numerical zeros with positive imaginary part.
Their coordinates and residuals are in `zeta-recorded.json`. To reproduce these
optional numbers in an isolated Python environment, install `mpmath==1.3.0`
and run `python3 zeta_map.py`. This is separate from the dependency-free Python
runner for the Lean controls. Four points do not prove the Riemann hypothesis.

- [NIST: zeta zeros and the critical strip](https://dlmf.nist.gov/25.10)
- [Clay Mathematics Institute: the Riemann hypothesis](https://www.claymath.org/millennium/riemann-hypothesis/)

- [OpenAI announcement, 6 October 2026](https://openai.com/index/sharing-ai-progress-in-mathematics/)
- [Pinned OpenAI release](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a)
- [Actual challenge configuration](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/QuasiRiemannHypothesis.json)
- [Actual solution entry point](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean)
- [Lean axioms and computation](https://lean-lang.org/theorem_proving_in_lean4/Axioms-and-Computation/)
- [Community discussion, 11 September 2026](https://terrytao.wordpress.com/2026/09/11/a-severe-misalignment-of-ai-in-mathematics/)

We inspected the OpenAI challenge and solution files; we did not rebuild their
dependency chain. A sorry placeholder in a challenge file is not by itself a
gap in the separate submitted solution. Their stated Re(s)>7/8 zero-free region
is not the full Riemann hypothesis. The internal model is unreleased.

Our scripts and diagrams are educational material. Formal correctness depends
on the exact statement, definitions, foundations and checker. It does not by
itself establish novelty, significance, or human understanding.

## Tested environment and troubleshooting

The four controls were reproduced on Linux aarch64 with Python 3.12 and Lean
4.34.1. Other OS/CPU combinations are not tested here. If the command is missing,
pass the full extracted Lean executable path with `--lean`. A different Lean
version is rejected so that changes in diagnostics do not look like the same run.
Failures of Broken.lean and False.lean are the expected negative controls.

Optional zeta example:

```sh
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install mpmath==1.3.0
python3 zeta_map.py
```

Share reproducible corrections through repository issues: include the Lean
version, the example, and the complete output. A different result is useful
evidence; it is not by itself a conclusion about the research release.

## License

Original code and teaching examples in this repository are MIT licensed.
The RUNTIME name, logo, video and narration are not licensed by this code license.
Linked OpenAI research and Lean software retain their own licenses.

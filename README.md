# Xeon Max 9470C Benchmarks

Interactive benchmark report for an Intel Xeon Max 9470C system with 52 cores / 104 threads and 64GB HBM2e. The original raw results are from local Phoronix Test Suite runs uploaded to OpenBenchmarking.org, with selected public comparison points added where they are available.

- Test date: 2026-05-30
- Last updated: 2026-06-03
- System: Intel Xeon Max 9470C, 52C/104T, 64GB HBM2e-3200, Ubuntu 24.04
- Power mode: `intel_pstate performance`, EPP `performance` where noted
- GPU present: NVIDIA RTX 3090, driver 595.71.05

## Interactive Report

Open the generated report locally:

```bash
python3 -m http.server 8080
```

Then open:

```text
http://localhost:8080/report/
```

The report is generated from `data/benchmarks.json` by `scripts/render_charts.py` and includes interactive charts for STREAM, compression, AI kernels, OpenVINO, LLM inference, molecular dynamics, CP2K, compile/FFT/y-cruncher, PyTorch, TensorFlow, SVT-AV1, spaCy, and other workloads.

## Abstract

The Xeon Max 9470C is a specialized CPU platform. Its clearest wins come from HBM memory bandwidth and Intel-optimized AI kernels. It is strongest in STREAM bandwidth, oneDNN BF16/INT8, PyTorch CPU inference, TensorFlow CPU inference, and OpenVINO GenAI throughput. Results are more mixed in classic OpenVINO INT8, y-cruncher, FFTW, spaCy transformer throughput, and vLLM CPU latency. General integer throughput, compile speed, heavy video encoding, QuantLib, and several HPC simulation workloads are less favorable versus high-clock desktop CPUs or modern dual-socket server platforms.

## Key Findings

Strong results:

- STREAM / HBM memory bandwidth
- oneDNN BF16 and INT8 convolution kernels
- PyTorch 2.11 CPU inference
- TensorFlow 2.21 CPU inference
- OpenVINO GenAI sustained throughput

Good or mixed results:

- OpenVINO classic INT8 inference
- y-cruncher 1B
- FFTW 1D 4096
- spaCy transformer pipeline
- vLLM CPU latency

Ordinary or weak for class:

- 7-Zip compression/decompression
- llama.cpp CPU BLAS
- GROMACS / LAMMPS / CP2K versus modern dual-socket servers
- QuantLib
- Linux kernel compile
- SVT-AV1 heavy 4K and 10-bit encoding
- spaCy `en_core_web_lg`

Not a platform-wide conclusion:

- NumPy 1.2.1, because the PTS profile is forced single-threaded.

## Original Result Links

These are the original 9470C result uploads used as the report baseline.

| Benchmark | Result URL |
| --- | --- |
| y-cruncher | https://openbenchmarking.org/result/2606027-NE-PHORONIX239 |
| NumPy | https://openbenchmarking.org/result/2606026-NE-NUMPY947030 |
| PyTorch | https://openbenchmarking.org/result/2606026-NE-PYTORCH9462 |
| TensorFlow | https://openbenchmarking.org/result/2606026-NE-BENCHMARK26 |
| OpenVINO GenAI | https://openbenchmarking.org/result/2606027-NE-OPENVINOG00 |
| vLLM CPU | https://openbenchmarking.org/result/2606012-NE-VLLMCPUHE78 |
| GROMACS | https://openbenchmarking.org/result/2606024-NE-GROMACS9487 |
| LAMMPS | https://openbenchmarking.org/result/2606025-NE-LAMMPS94755 |
| CP2K | https://openbenchmarking.org/result/2606037-NE-PLSCP2K9443 |
| QuantLib | https://openbenchmarking.org/result/2606027-NE-BENCHMARK83 |
| Linux kernel compile | https://openbenchmarking.org/result/2606021-NE-PHORONIXT83 |
| FFTW | https://openbenchmarking.org/result/2606028-NE-PHORONIXT90 |
| SVT-AV1 | https://openbenchmarking.org/result/2606031-NE-AV19470C958 |
| spaCy | https://openbenchmarking.org/result/2606034-NE-SPACY947003 |

## Included Charts

The interactive report currently includes 18 chart groups:

- STREAM 2013 memory bandwidth
- 7-Zip CPU throughput
- oneDNN BF16 / INT8 convolution kernels
- oneDNN FP16 / FP32 limited comparison
- OpenVINO 2026.0 CPU inference
- OpenVINO GenAI CPU throughput
- OpenVINO GenAI time to first token
- llama.cpp CPU BLAS
- vLLM CPU Hermes 3B
- GROMACS and LAMMPS molecular dynamics
- CP2K molecular dynamics
- QuantLib
- Linux compile / FFTW / y-cruncher
- NumPy single-threaded score
- PyTorch 2.11 CPU inference
- TensorFlow 2.21 CPU inference
- SVT-AV1 CPU encoding
- spaCy NLP throughput

## Repository Layout

```text
data/benchmarks.json      Structured benchmark data and source links
scripts/render_charts.py  Static report/chart generator
report/index.html         Generated interactive HTML report
README.md                 Project overview and links
```

## Regenerate

```bash
python3 scripts/render_charts.py
```

The generator uses only Python standard library modules. No frontend build step is required.

## Data Notes

- Local values are from the linked OpenBenchmarking result uploads and the local benchmark notes captured in this repository.
- Public comparison values are taken from OpenBenchmarking/Phoronix output, OpenBenchmarking profile summaries, or public comparison pages listed in the report footer.
- Missing comparison values are not fabricated. When a benchmark has limited comparison coverage, the chart says so directly.
- Some charts convert lower-is-better raw timings into relative speed for visual consistency. In those cases the original seconds or milliseconds remain visible in the value labels.

# Xeon Max 9470C Benchmark Summary

Date: 2026-05-30  
Last updated: 2026-06-03  
System: Intel Xeon Max 9470C, 52C/104T, 64GB HBM2-3200, Ubuntu 24.04, intel_pstate performance with EPP performance  
Y-Cruncher result URL: https://openbenchmarking.org/result/2606027-NE-PHORONIX239  
NumPy result URL: https://openbenchmarking.org/result/2606026-NE-NUMPY947030  
PyTorch result URL: https://openbenchmarking.org/result/2606026-NE-PYTORCH9462  
TensorFlow result URL: https://openbenchmarking.org/result/2606026-NE-BENCHMARK26  
OpenVINO GenAI result URL: https://openbenchmarking.org/result/2606027-NE-OPENVINOG00  
vLLM CPU result URL: https://openbenchmarking.org/result/2606012-NE-VLLMCPUHE78  
GROMACS result URL: https://openbenchmarking.org/result/2606024-NE-GROMACS9487  
LAMMPS result URL: https://openbenchmarking.org/result/2606025-NE-LAMMPS94755  
CP2K result URL: https://openbenchmarking.org/result/2606037-NE-PLSCP2K9443  
QuantLib result URL: https://openbenchmarking.org/result/2606027-NE-BENCHMARK83  
Linux Kernel Compile result URL: https://openbenchmarking.org/result/2606021-NE-PHORONIXT83  
FFTW result URL: https://openbenchmarking.org/result/2606028-NE-PHORONIXT90  
SVT-AV1 result URL: https://openbenchmarking.org/result/2606031-NE-AV19470C958  
GPU: NVIDIA RTX 3090, driver 595.71.05

## Summary Table

Values are from local Phoronix Test Suite runs compared side-by-side with the most relevant reference CPUs printed in the corresponding OpenBenchmarking.org benchmark outputs.

| Benchmark | 9470C Result | Comparison Reference(s) | Percentile / Conclusion |
| --- | ---: | --- | --- |
| STREAM Copy | 658,763 MB/s | Desktop DDR5 Dual-Ch (~60k-80k MB/s), Xeon 8490H (8-Ch DDR5-4800): 270k MB/s, EPYC 9654 (12-Ch DDR5-4800): 380k MB/s, EPYC 9755 (12-Ch DDR5-6000): 480k MB/s, 2x EPYC 9755 (24-Ch DDR5-6000): 960k MB/s | 10x faster HBM bandwidth is the platform's clearest strength |
| 7-Zip Compression | 351,346 MIPS | EPYC 9755: 1,123,940 MIPS, EPYC 9655P: ~520,000 MIPS, TR 9980X: ~428,047 MIPS, R9 9950X: ~188,000 MIPS, Core i9-14900K: ~172,000 MIPS | Good, but not a top-tier general integer throughput result |
| 7-Zip Decompression | 205,861 MIPS | EPYC 9755: 831,688 MIPS, EPYC 9655P: ~480,000 MIPS, TR 9980X: ~513,073 MIPS, R9 9950X: ~158,000 MIPS, Core i9-14900K: ~146,800 MIPS | Decompression is a relative weak spot |
| oneDNN BF16 Conv | 44,155 GFLOPS | 2x EPYC 9475F: 34,979 GFLOPS, 2x EPYC 9455: 32,464 GFLOPS, EPYC 9755: ~26,000 GFLOPS, TR 9980X: 22,383 GFLOPS, Ryzen 9 9950X: ~3,500 GFLOPS | 93rd percentile; AMX/BF16 is a major strength |
| oneDNN INT8 Conv | 105,713 GFLOPS | 2x EPYC 9475F: 64,073 GFLOPS, 2x EPYC 9455: 59,409 GFLOPS, EPYC 9755: 53,335 GFLOPS, TR 9980X: 41,748 GFLOPS, Ryzen 9 9950X: 14,602 GFLOPS | 93rd percentile; AMX/INT8 is a major strength |
| OpenVINO Face INT8 | 208 FPS | EPYC 9755: ~193 FPS, 2x EPYC 9755: 410 FPS, 2x EPYC 9655: 312 FPS, 2x Xeon 6980P: 867 FPS, TR 9980X: ~145 FPS | 79th percentile; strong small-model CPU inference |
| OpenVINO Vehicle INT8 | 3,285 FPS | EPYC 9755: 10,894 FPS, 2x EPYC 9755: 19,694 FPS, 2x EPYC 9655: 14,655 FPS, 2x Xeon 6980P: 13,534 FPS, TR 9980X: ~2,400 FPS | 59th percentile; complex-model throughput trails high-end EPYC/Xeon |
| OpenVINO Road INT8 | 900 FPS | EPYC 9755: 3,362 FPS, 2x EPYC 9755: 6,931 FPS, 2x EPYC 9655: 5,117 FPS, 2x Xeon 6980P: 4,406 FPS, TR 9980X: ~650 FPS | 57th percentile; complex segmentation throughput trails modern EPYC |
| llama.cpp granite 3B PP2048 | 239.83 tok/s | TR 7980X: 412 tok/s, 2x EPYC 9275F: 447 tok/s, 2x EPYC 9475F: 573 tok/s, 2x EPYC 9565: 654 tok/s, Ryzen 9 9950X: ~135 tok/s | CPU LLM inference via llama.cpp BLAS is mediocre |
| vLLM CPU Hermes 3B Latency | 4.10 s | EPYC 9755: 5.53 s, TR 7980X: 9.93 s, R9 9950X3D: 15.60 s, EPYC 9745: ~6.20 s, Core i9-14900K: ~18.50 s | Strong low-latency CPU LLM result (beats EPYC 9755) |
| vLLM CPU Hermes 3B Throughput | 235.14 tok/s | EPYC 9755: 392 tok/s, EPYC 9745: 371 tok/s, EPYC 9655P: 339 tok/s, EPYC 4585PX: 144 tok/s, TR 7980X: ~220 tok/s | Throughput trails modern server platforms |
| OpenVINO GenAI Qwen3-8B CPU | 25.46 tok/s | EPYC 9755: 24.99 tok/s, EPYC 9745: 21.79 tok/s, EPYC 9555P: 23.36 tok/s, TR 7980X: 15.02 tok/s, Ryzen 9 9950X: 5.90 tok/s | 83rd percentile; beats EPYC 9755 and TR 7980X |
| OpenVINO GenAI Qwen2.5-1.5B CPU | 63.72 tok/s | EPYC 9755: 61.10 tok/s, EPYC 9745: 51.95 tok/s, TR 7980X: 54.65 tok/s, Ryzen 9 9950X: 26.65 tok/s, 2x EPYC 9655: 68 tok/s | 80th percentile; beats EPYC 9755 and TR 7980X |
| OpenVINO GenAI granite 8B CPU | 19.97 tok/s | EPYC 9755: 24.05 tok/s, EPYC 9745: 21.03 tok/s, TR 7980X: 13.95 tok/s, Ryzen 9 9950X: 5.51 tok/s, 2x EPYC 9965: 16.41 tok/s | 66th percentile; beats TR 7980X but trails EPYC 9755 |
| GROMACS water_GMX50 | 7.796 ns/day | 2x EPYC 9755: 39.52 ns/day, 2x EPYC 9965: 38.10 ns/day, 2x Xeon 6980P: 35.42 ns/day, 2x EPYC 9655: 31.92 ns/day, EPYC 9755 (1x): ~20.00 ns/day | 69th percentile; above median but far behind large current servers |
| LAMMPS 20k Atoms | 25.818 ns/day | 2x EPYC 9965: 125 ns/day, 2x EPYC 9655: 106 ns/day, EPYC 9755: 82 ns/day, EPYC 9754: 48.14 ns/day, EPYC 4585PX: 21.61 ns/day | 51st percentile; around median; not an HBM showcase |
| CP2K H20-64 (lower is better) | 38.253 s | 2x EPYC 9755: 14.12 s, 2x EPYC 9965: 21.35 s, Ryzen 9 9900X3D: 45.29 s, 4x EPYC 9V64H: 50.22 s, EPYC 7F32: 92 s | 53rd percentile; near median |
| CP2K H20-256 (lower is better) | 306.749 s | 2x Xeon 6980P: 80 s, 2x EPYC 9535: 129 s, 2x EPYC 9845: 221 s, 4x EPYC 9V64H: 348 s, Xeon Silver 4216: 918 s | 57th percentile; above median but trails dual-socket servers |
| QuantLib S | 26.84 tasks/s | 2x EPYC 9755: 198 tasks/s, 2x Xeon 6980P: 161 tasks/s, 2x EPYC 9655: 139 tasks/s, 2x EPYC 9555: 116 tasks/s, 2x Xeon 6780E: 97 tasks/s | 42nd percentile; quant finance is not a 9470C strength |
| Linux Kernel Compile (lower is better) | 506.062 s | EPYC 9575F: 257 s, EPYC 8324P: 705 s, EPYC 8224P: 966 s, EPYC 8224PN: 1123 s, Ryzen AI 9 365: 2118 s | 57th percentile; compile speed is decent but not a showcase |
| FFTW Float+SSE 1D 4096 | 65,223 Mflops | Ryzen 9 7950X: 97,828 Mflops, Core i7-11700K: 85,852 Mflops, Core i9-14900K: 83,438 Mflops, Core i5-12600K: 78,169 Mflops, Xeon Gold 6414U: 63,218 Mflops | 88th percentile; strong scientific FFT result, beats Xeon Gold |
| y-cruncher 1B (lower is better) | 7.605 s | 2x Xeon 6980P: 2.86 s, 2x EPYC 9745: 5.56 s, TR 7980X: 10.91 s, R9 7950X3D: 15.80 s, R7 5800X3D: 37.91 s | 77th percentile; beats 64C Threadripper and all desktop CPUs |
| NumPy (single-threaded) | 472 Score | EPYC 4585PX: 1,098, 2x EPYC 9575F: 982, Ryzen 7 7800X3D: 785, Core i9-9900KS: 447, EPYC 7F52: 351 | 56th percentile; forced single-threaded; not a meaningful benchmark |
| PyTorch ResNet-50 bs=1 | 247.14 batches/s | R9 9950X3D2: 120 batches/s, TR 9980X: ~91 batches/s, EPYC 9455P: ~88 batches/s, Core Ultra 7 270K+: ~85 batches/s, R9 9900X3D: ~80 batches/s | OpenBenchmarking High; leads best desktop by 2x and 64C HEDT by 2.7x |
| TensorFlow ResNet-50 bs=64 CPU | 177.11 img/s | 2x EPYC 9655: 277 img/s, TR 9980X: 116 img/s, TR 7980X: 78 img/s, Ryzen 9 9950X: ~45 img/s, Core i9-14900K: ~52 img/s | 90th percentile; strong CPU deep-learning result |
| TensorFlow ResNet-50 bs=128 CPU | 183.29 img/s | 2x EPYC 9655: 326 img/s, TR 9980X: 125 img/s, TR 7980X: 83 img/s, Ryzen 9 9950X: ~48 img/s, Core i9-14900K: ~55 img/s | 90th percentile; strong CPU deep-learning result |
| SVT-AV1 Preset 5 Bosphorus 4K | 46.57 FPS | 2x EPYC 9755: 93.00 FPS, TR 9980X: 96.00 FPS, R9 9950X3D: 71.00 FPS, R9 9950X: 62.00 FPS, Core Ultra 7 270K+: 54.27 FPS | 41st percentile; ordinary for its class; lower boost clock |
| SVT-AV1 Preset 8 Bosphorus 4K | 121.40 FPS | EPYC 9755: 234.00 FPS, 2x EPYC 9655: 230.00 FPS, R9 9950X3D: 170.00 FPS, Core Ultra 7 270K+: 157.00 FPS, Core i9-14900K: 128.00 FPS | 40th percentile; ordinary; clock scales moderately here |
| SVT-AV1 Preset 13 Bosphorus 4K | 226.55 FPS | EPYC 9655P: 452.00 FPS, 2x EPYC 9355: 380.00 FPS, R9 9950X3D: 281.00 FPS, R9 9900X3D: 260.00 FPS, Core i9-10980XE: 144.00 FPS | 43rd percentile; trails EPYC 9655P and TR 9950X3D |
| SVT-AV1 Preset 5 Bosphorus 1080p | 135.80 FPS | 2x EPYC 9755: 266.00 FPS, EPYC 9655P: 273.00 FPS, TR 9980X: 258.00 FPS, R9 9950X: 221.00 FPS, Core i9-14900K: 145.00 FPS | 64th percentile; strong showing for lighter 1080p encoding |
| SVT-AV1 Preset 8 Bosphorus 1080p | 321.49 FPS | EPYC 9655P: 641.00 FPS, EPYC 9755: 622.00 FPS, 2x EPYC 9755: 607.00 FPS, R9 9950X3D: 594.00 FPS, R9 9950X: 440.00 FPS | 61st percentile; good core scaling on lighter density |
| SVT-AV1 Preset 13 Bosphorus 1080p | 682.14 FPS | EPYC 9655P: 1419.00 FPS, 2x EPYC 9755: 1356.00 FPS, TR 9980X: 1264.00 FPS, R9 9950X: 794.00 FPS, Core Ultra 5 245K: 761.00 FPS | 61st percentile; high core count scales well for lighter 1080p |
| SVT-AV1 Preset 5 Beauty 4K 10-bit | 7.85 FPS | TR PRO 9995WX: 12.69 FPS, EPYC 9655P: 12.47 FPS, EPYC 9555P: 12.14 FPS, R9 9950X3D: 11.93 FPS, 2x Xeon 6780E: 5.36 FPS | 32nd percentile; heavy 10-bit encoding drops CPU performance |
| SVT-AV1 Preset 8 Beauty 4K 10-bit | 10.43 FPS | R9 9950X3D2: 18.27 FPS, Core Ultra 7 270K+: 18.15 FPS, R9 9950X: 17.40 FPS, EPYC 9755: 15.14 FPS, TR 3990X: 10.16 FPS | 23rd percentile; low boost clock limits heavy 10-bit encoding |
| SVT-AV1 Preset 13 Beauty 4K 10-bit | 12.11 FPS | R9 9950X3D2: 21.58 FPS, TR PRO 9975WX: 20.90 FPS, R9 9950X: 20.64 FPS, EPYC 9755: 17.69 FPS, TR 3990X: 11.72 FPS | 22nd percentile; low clock speed limits heavy 10-bit loops |

## Local Results

### STREAM 2013

| Subtest | 9470C |
| --- | ---: |
| Copy | 658,763.5 MB/s |
| Scale | 651,040.3 MB/s |
| Triad | 596,258.8 MB/s |
| Add | 606,724.4 MB/s |

Interpretation: this is the best evidence of the Xeon Max platform advantage. The result is about 600-660 GB/s on STREAM, far above normal dual-channel desktop DDR5 and competitive with large multi-channel server DDR5 configurations.

### 7-Zip Compression

| Subtest | 9470C |
| --- | ---: |
| Compression | 351,346 MIPS |
| Decompression | 205,861 MIPS |

Performance-governor rerun:

| Subtest | 9470C |
| --- | ---: |
| Compression | 352,387 MIPS |
| Decompression | 202,761 MIPS |

Interpretation: performance mode improved stability but did not materially change the score. 7-Zip is not the 9470C's best workload.

### oneDNN 3.12

| Subtest | 9470C | Percentile |
| --- | ---: | ---: |
| Convolution Batch Shapes BF16 CPU | 44,155 GFLOPS | 93rd |
| Convolution Batch Shapes FP16 CPU | 3,570 GFLOPS | n/a |
| Convolution Batch Shapes FP32 CPU | 5,584 GFLOPS | 58th |
| Convolution Batch Shapes INT8 CPU | 105,713 GFLOPS | 93rd |

Interpretation: BF16 and INT8 are the strongest AI-kernel results so far. This is where AMX/VNNI show up clearly.

### OpenVINO 2026.0

| Model / Mode | 9470C | Percentile |
| --- | ---: | ---: |
| Face Detection FP16-INT8, Latency | 115 FPS / 34.73 ms | 82nd FPS / 43rd latency |
| Face Detection FP16-INT8, Throughput | 208 FPS / 249.62 ms | 79th FPS / 48th latency |
| Vehicle Detection FP16-INT8, Latency | 2,057 FPS / 1.94 ms | 91st FPS / 29th latency |
| Vehicle Detection FP16-INT8, Throughput | 3,285 FPS / 15.78 ms | 59th FPS / 12th latency |
| Road Segmentation ADAS FP16-INT8, Latency | 681 FPS / 5.87 ms | 76th FPS / 21st latency |
| Road Segmentation ADAS FP16-INT8, Throughput | 900 FPS / 57.73 ms | 57th FPS / 5th latency |

Interpretation: OpenVINO is mixed. Small INT8 detection looks good, but complex-model throughput is not competitive with high-end EPYC/Xeon server platforms.

### llama.cpp b4154

| Test | 9470C |
| --- | ---: |
| CPU BLAS, granite-3.0-3b-a800m-instruct-Q8_0, Prompt Processing 2048 | 239.83 tokens/s |

Interpretation: llama.cpp CPU BLAS does not expose the same advantage seen in oneDNN BF16/INT8. This is a weak-to-average result for this CPU class.

### vLLM CPU 0.15.1

Result URL: https://openbenchmarking.org/result/2606012-NE-VLLMCPUHE78

Configuration notes:

- Profile: `pts/vllm-cpu-1.0.0`
- Model: `NousResearch/Hermes-3-Llama-3.2-3B`
- Local cache: `/mnt/PM983/cache/huggingface`
- CPU binding: 52 physical cores, logical CPUs `0-51`
- NUMA policy: interleave across nodes `0-3`
- KV cache setting: `VLLM_CPU_KVCACHE_SPACE=16`
- Power mode: `intel_pstate performance`, EPP `performance`

Latency:

| Metric | 9470C | EPYC 9755 | Threadripper 7980X | Ryzen 9 9950X3D |
| --- | ---: | ---: | ---: | ---: |
| Average latency | 4.10 s | 5.53 s | 9.93 s | 15.6 s |
| 10p latency | 4.05 s | 5.52 s | 9.93 s | 15.58 s |
| 50p latency | 4.09 s | 5.53 s | 9.93 s | 15.60 s |
| 75p latency | 4.13 s | 5.52 s | 9.93 s | 15.61 s |
| 90p latency | 4.15 s | 5.52 s | 9.94 s | 15.63 s |
| 99p latency | 4.21 s | 5.54 s | 9.94 s | 15.64 s |

Throughput:

| Metric | 9470C | EPYC 9755 | EPYC 9745 | EPYC 9655P | EPYC 4585PX |
| --- | ---: | ---: | ---: | ---: | ---: |
| Requests/s | 1.57 | 2.61 | n/a | n/a | 0.96 |
| Tokens/s | 235.14 | 392 | 371 | 339 | 144 |

Interpretation: vLLM CPU is split. The 9470C is excellent on the latency side and beats the listed EPYC 9755 latency result, but it trails modern EPYC in high-concurrency throughput. The throughput profile pushes 1000 requests and drives KV cache usage close to 100%, so it is closer to a saturated serving stress test than a simple single-request token/s test.

Manual large-prompt prefill check, not an OpenBenchmarking database result:

| Input tokens | Output tokens | Batch | Avg latency | vLLM native prompt throughput |
| ---: | ---: | ---: | ---: | ---: |
| 512 | 1 | 1 | 0.238 s | n/a |
| 2048 | 1 | 1 | 1.008 s | n/a |
| 4096 | 1 | 1 | 2.797 s | 1456.6 tokens/s |

Notes: this was run with `vllm bench latency`, `dtype=bfloat16`, `max-model-len=8192`, CPU target, 52 OMP threads bound to cores `0-51`, and `enable_chunked_prefill=True`. The 4096-token run emitted vLLM's native backend logger line: `Avg prompt throughput: 1456.6 tokens/s`. The shorter 512/2048 runs finished before the periodic backend throughput logger fired, so only their latency values are recorded.

### OpenVINO GenAI 2026.0

Result URL: https://openbenchmarking.org/result/2606027-NE-OPENVINOG00

Additional cloned online result sets:

- EPYC 9755 / EPYC 9745: https://openbenchmarking.org/result/2603029-NE-AMDEPYC1265
- Threadripper 7980X: https://openbenchmarking.org/result/2603012-PTS-MARCH39979
- Ryzen 9 9950X: https://openbenchmarking.org/result/2603199-PTS-POPOS24068

Configuration:

- Profile: `pts/openvino-genai-1.3.0`
- Device: CPU
- Models: `Qwen3-8B`, `Qwen2.5-1.5B-Instruct`, `granite-3.0-8b-instruct`
- Power note: Phoronix still reported governor as `intel_pstate powersave`, but EPP was `performance`.

| Model | Throughput | Percentile | Time To First Token | TTFT Percentile |
| --- | ---: | ---: | ---: | ---: |
| Qwen3-8B | 25.46 tokens/s | 83rd | 74.01 ms | 60th |
| Qwen2.5-1.5B-Instruct | 63.72 tokens/s | 80th | 35.61 ms | 23rd |
| granite-3.0-8b-instruct | 19.97 tokens/s | 66th | 83.36 ms | 59th |

Comparison labels shown by OpenBenchmarking:

| Model | 9470C | Nearby / stronger references |
| --- | ---: | --- |
| Qwen3-8B | 25.46 tokens/s | EPYC 9745: 21.75; EPYC 9555P: 23.36; EPYC 9655P: 26.8; 2 x EPYC 9655: 28.6; 2 x EPYC 9555: 34.52 |
| Qwen2.5-1.5B-Instruct | 63.72 tokens/s | Threadripper 7980X: 54.66; EPYC 9755: 61; 2 x EPYC 9655: 68; 2 x EPYC 9555: 79; 2 x EPYC 9455: 83 |
| granite-3.0-8b-instruct | 19.97 tokens/s | Threadripper 7980X: 13.94; 2 x EPYC 9965: 16.41; Threadripper 9980X: 18.02; EPYC 9745: 21.01; 2 x EPYC 9555: 32.01 |

Additional exact online comparisons cloned from OpenBenchmarking result files:

| Model | 9470C | EPYC 9755 | EPYC 9745 | TR 7980X | Ryzen 9 9950X |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3-8B throughput | 25.46 tok/s | 24.99 tok/s | 21.79 tok/s | 15.02 tok/s | 5.90 tok/s |
| Qwen2.5-1.5B throughput | 63.72 tok/s | 61.10 tok/s | 51.95 tok/s | 54.65 tok/s | 26.65 tok/s |
| granite-3.0-8B throughput | 19.97 tok/s | 24.05 tok/s | 21.03 tok/s | 13.95 tok/s | 5.51 tok/s |
| Qwen3-8B TTFT | 74.01 ms | 50.33 ms | 56.49 ms | 78.15 ms | 178.00 ms |
| Qwen2.5-1.5B TTFT | 35.61 ms | 23.47 ms | 26.60 ms | 25.78 ms | 43.69 ms |
| granite-3.0-8B TTFT | 83.36 ms | 54.33 ms | 60.02 ms | 86.94 ms | 190.91 ms |

Interpretation: OpenVINO GenAI is the strongest CPU LLM benchmark so far for this platform. Unlike llama.cpp BLAS, it shows the 9470C landing in the upper range of the OpenBenchmarking database for throughput. Against exact cloned online results, the 9470C beats Threadripper 7980X and Ryzen 9 9950X decisively, and it is close to single-socket EPYC 9755: faster on Qwen3 and Qwen2.5-1.5B throughput, slower on granite. TTFT is mixed: EPYC has better first-token latency, while the 9470C's strength is sustained token throughput.

### GROMACS 2025.4

Result URL: https://openbenchmarking.org/result/2606024-NE-GROMACS9487

| Test | 9470C | Percentile |
| --- | ---: | ---: |
| MPI CPU, water_GMX50_bare | 7.796 ns/day | 69th |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| 2 x EPYC 9755 | 39.52 ns/day |
| 2 x EPYC 9965 | 38.1 ns/day |
| 2 x Xeon 6980P | 35.42 ns/day |
| 2 x EPYC 9655 | 31.92 ns/day |

Interpretation: GROMACS is a useful real HPC molecular-dynamics check. The 9470C is above the current sample median, but it does not approach modern dual-socket EPYC/Xeon server results in this profile.

### LAMMPS 22Jul2025 Update 2

Result URL: https://openbenchmarking.org/result/2606025-NE-LAMMPS94755

| Test | 9470C | Percentile |
| --- | ---: | ---: |
| 20k Atoms | 25.818 ns/day | 51st |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| 2 x EPYC 9965 | 125 ns/day |
| 2 x EPYC 9655 | 106 ns/day |
| 2 x Xeon 6980P | 95 ns/day |
| 2 x EPYC 9555 | 89 ns/day |
| EPYC 9755 | 82 ns/day |
| EPYC 9555P | 52.32 ns/day |
| EPYC 9754 | 48.14 ns/day |
| EPYC 4585PX | 21.61 ns/day |
| EPYC 7551 | 12.821 ns/day |

Interpretation: LAMMPS 20k Atoms is around the database median. It beats older/lower-end EPYC samples shown in the comparison output, but trails current high-core EPYC and dual-socket servers by a large margin.

### CP2K Molecular Dynamics 2024.3

Result URL: https://openbenchmarking.org/result/2606037-NE-PLSCP2K9443

Configuration:

- Profile: `pts/cp2k-1.5.0`
- Inputs: `H20-64`, `H20-256`
- Power state: `intel_pstate performance`, EPP `performance`
- Lower is better.

| Input | 9470C | Percentile | Median |
| --- | ---: | ---: | ---: |
| H20-64 | 38.253 s | 53rd | 42.14 s |
| H20-256 | 306.749 s | 57th | 417 s |

Comparison labels shown by OpenBenchmarking:

| Input | Reference | Result |
| --- | --- | ---: |
| H20-64 | 2 x EPYC 9755 | 14.119 s |
| H20-64 | 2 x EPYC 9965 | 21.35 s |
| H20-64 | EPYC 7F32 | 92 s |
| H20-64 | Ryzen 9 9900X3D | 45.29 s |
| H20-64 | 4 x EPYC 9V64H | 50.22 s |
| H20-256 | 2 x Xeon 6980P | 80 s |
| H20-256 | 2 x EPYC 9535 | 129 s |
| H20-256 | 2 x EPYC 9845 | 221 s |
| H20-256 | 4 x EPYC 9V64H | 348 s |
| H20-256 | Xeon Silver 4216 | 918 s |

Interpretation: CP2K is only a modest win for the 9470C. H20-64 lands almost exactly around the database middle, while H20-256 is better at 57th percentile and clearly above the median. It can beat some older or unusual server references, but it is far behind modern dual-socket EPYC/Xeon systems. This looks more like a mixed MPI/OpenMP scientific workload than a pure HBM showcase.

### QuantLib 1.39

Result URL: https://openbenchmarking.org/result/2606027-NE-BENCHMARK83

Configuration:

- Profile: `pts/quantlib-2.2.0`
- Size: `S`
- Power note: Phoronix still reported governor as `intel_pstate powersave`, with EPP `performance`.

| Test | 9470C | Percentile | Median |
| --- | ---: | ---: | ---: |
| QuantLib Benchmark Index, Size S | 26.8421 tasks/s | 42nd | 43.29 tasks/s |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| 2 x EPYC 9755 | 198 tasks/s |
| 2 x Xeon 6980P | 161 tasks/s |
| 2 x EPYC 9655 | 139 tasks/s |
| 2 x EPYC 9555 | 116 tasks/s |
| 2 x Xeon 6780E | 97 tasks/s |

Interpretation: QuantLib is not a strong 9470C workload in this profile. The local run is stable, but only 42nd percentile and well below the current OpenBenchmarking median. This benchmark is a C++ quantitative-finance workload using Boost IPC parallelism; it does not look like an AMX/HBM showcase. It is more sensitive to general CPU throughput, scheduling, Boost IPC overhead, frequency behavior, and the exact scaling shape of the test. Because Phoronix warned that the governor was not set to `performance`, this result is worth one confirmation rerun after forcing the governor.

### Timed Linux Kernel Compilation 7.0

Result URL: https://openbenchmarking.org/result/2606021-NE-PHORONIXT83

Configuration:

- Profile: `pts/build-linux-kernel-1.18.0`
- Build: `allmodconfig`
- Power note: Phoronix still reported governor as `intel_pstate powersave`, with EPP `performance`.

| Run | 9470C |
| --- | ---: |
| Run 1 | 508.062 s |
| Run 2 | 506.707 s |
| Run 3 | 503.418 s |
| Average | 506.062 s |
| Percentile | 57th |
| Median | 617 s |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| EPYC 9575F | 257 s |
| EPYC 8324P | 705 s |
| EPYC 8224P | 966 s |
| EPYC 8224PN | 1123 s |
| Ryzen AI 9 365 | 2118 s |

Interpretation: Linux kernel `allmodconfig` compile is decent but not a 9470C showcase. The score is above median and much faster than lower-core EPYC 8004 examples, but far behind frequency-optimized/high-throughput Zen 5 parts like EPYC 9575F. This workload does not use AMX and is not primarily limited by peak HBM bandwidth. It is closer to a mixed compile workload: per-core compiler throughput, cache behavior, branchy integer work, process scheduling, and filesystem/cache cleanup all matter. Because the run still triggered the Phoronix governor warning, it is worth a confirmation rerun after forcing `scaling_governor=performance`.

### FFTW 3.3.6

Result URL: https://openbenchmarking.org/result/2606028-NE-PHORONIXT90

Configuration:

- Profile: `pts/fftw-1.2.0`
- Build: `Float + SSE`
- Size: `1D FFT Size 4096`
- Power state: `intel_pstate performance`, EPP `performance`

| Run | 9470C |
| --- | ---: |
| Run 1 | 68,712 Mflops |
| Run 2 | 58,416 Mflops |
| Run 3 | 61,478 Mflops |
| Run 4 | 66,440 Mflops |
| Run 5 | 66,859 Mflops |
| Run 6 | 65,656 Mflops |
| Run 7 | 66,691 Mflops |
| Run 8 | 62,462 Mflops |
| Run 9 | 65,626 Mflops |
| Run 10 | 65,570 Mflops |
| Run 11 | 67,482 Mflops |
| Run 12 | 67,505 Mflops |
| Run 13 | 63,942 Mflops |
| Run 14 | 64,113 Mflops |
| Run 15 | 67,387 Mflops |
| Average | 65,223 Mflops |
| Deviation | 4.19% |
| Percentile | 88th |
| Median | 41,810 Mflops |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| Ryzen 9 7950X | 97,828 Mflops |
| Core i7-11700K | 85,852 Mflops |
| Core i9-14900K | 83,438 Mflops |
| Core i5-12600K | 78,169 Mflops |
| Xeon Gold 6414U | 63,218 Mflops |
| Atom E3845 | 3,950 Mflops |

Interpretation: FFTW is a strong result and much better aligned with the 9470C than QuantLib or kernel compilation. The score lands in the 88th percentile and beats the nearby Xeon Gold 6414U reference. However, this selected FFTW variant is `Float + SSE`, not AVX2/AVX512, so it still does not fully expose the platform's AVX-512 potential. High-frequency desktop CPUs such as Ryzen 9 7950X and Core i9-14900K remain ahead on this particular small 1D FFT test. Larger 2D FFT sizes or explicit AVX512 variants should be tested next to see whether HBM and wide vectors change the picture.

### y-cruncher 0.8.5

Result URL: https://openbenchmarking.org/result/2606027-NE-PHORONIX239

| Run | 9470C |
| --- | ---: |
| Run 1 | 7.484 s |
| Run 2 | 7.671 s |
| Run 3 | 7.660 s |
| Average | 7.605 s |
| Percentile | 77th |
| Median (n=374) | 18.18 s |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| 2 x Xeon 6980P | 2.859 s |
| 2 x EPYC 9745 | 5.559 s |
| Threadripper 7980X | 10.911 s |
| Ryzen 9 7950X3D | 15.8 s |
| Ryzen 7 5800X3D | 37.91 s |

Interpretation: y-cruncher is a strong result for a single-socket platform. The 9470C easily beats the 64C Threadripper 7980X and all consumer desktop CPUs. It cannot match dual-socket 128C EPYC/Xeon servers, but the 77th percentile in a 374-sample database is solid. AVX-512 and strong memory bandwidth (HBM) both contribute here.

### NumPy 1.2.1

Result URL: https://openbenchmarking.org/result/2606026-NE-NUMPY947030

| Run | 9470C |
| --- | ---: |
| Run 1 | 474.00 |
| Run 2 | 474.12 |
| Run 3 | 469.10 |
| Average | 472.41 |
| Percentile | 56th |
| Median (n=3,990) | 430 |

Comparison labels shown by OpenBenchmarking:

| Reference | Result |
| --- | ---: |
| EPYC 4585PX | 1,098 |
| EPYC 4245P | 1,067 |
| 2 x EPYC 9575F | 982 |
| EPYC 9575F | 962 |
| Ryzen 7 7800X3D | 785 |
| Core i9-9900KS | 447 |
| Ryzen 7 3700X | 416 |
| EPYC 7F52 | 351 |
| 2 x EPYC 7F72 | 326 |

Interpretation: this result is limited by the benchmark's design, not the CPU. The PTS NumPy profile hard-codes `OMP_NUM_THREADS=1`, forcing single-threaded execution. The 9470C performs at roughly Core i9-9900KS (8-core desktop) level in this constrained mode. This is not a meaningful platform benchmark — it tests single-core Python/numpy speed and ignores all 104 threads and HBM bandwidth.

### PyTorch 2.11

Result URL: https://openbenchmarking.org/result/2606026-NE-PYTORCH9462

Configuration: batch sizes 1/64/512, all three model variants. This is a relatively new benchmark (April 2026) with a small database of 22-74 samples per subtest. Most comparison points are consumer desktop CPUs, but workstation-class data (EPYC 9455P, Threadripper 7980X/9980X) is present. No dual-socket EPYC or Xeon 6 data exists yet.

| Test | 9470C | Strongest Comparison | Type | Ratio |
| --- | ---: | ---: | ---: | ---: |
| ResNet-50 bs=1 | 247.14 | TR 9980X: 91 | 64C HEDT | 2.7x |
| ResNet-152 bs=1 | 86.82 | Core Ultra 7 270K+: 44.37 | 20C Desktop | 2.0x |
| ResNet-50 bs=64 | 153.61 | EPYC 9455P: 71.12 | 48C Server | 2.2x |
| ResNet-50 bs=512 | 153.24 | R9 9950X3D2: 77.46 | 16C Desktop | 2.0x |
| ResNet-152 bs=64 | 59.17 | R9 9950X3D2: 28.13 | 16C Desktop | 2.1x |
| ResNet-152 bs=512 | 58.84 | R9 9950X3D2: 28.42 | 16C Desktop | 2.1x |
| EfficientNet-v2-l bs=1 | 55.48 | R9 9900X3D: 22.44 | 12C Desktop | 2.5x |
| EfficientNet-v2-l bs=64 | 37.57 | R9 9950X3D2: 15.88 | 16C Desktop | 2.4x |
| EfficientNet-v2-l bs=512 | 37.76 | Core Ultra 7 270K+: 18.42 | 20C Desktop | 2.0x |

Interpretation: PyTorch CPU inference is a clear platform strength. The 9470C sets the highest score across all subtests in the OpenBenchmarking database. Against the only server-class comparison available (EPYC 9455P, 48-core Zen5), the 9470C leads by 2.2x. Against Threadripper 7980X/9980X (64-core HEDT), it leads by 2.0-2.7x. The database currently lacks dual-socket EPYC/Xeon 6 results, so absolute positioning against top-end servers isn't yet measurable. AMX INT8 acceleration and 104 threads both contribute to the strong showing.

### TensorFlow 2.21

Result URL: https://openbenchmarking.org/result/2606026-NE-BENCHMARK26

Configuration:

- Profile: `pts/tensorflow-2.4.0`
- Device: CPU
- Batch sizes: 64, 128
- Models: VGG-16, ResNet-50, AlexNet, GoogLeNet
- Power state: `intel_pstate performance`, EPP `performance`

| Model / Batch | 9470C | Percentile |
| --- | ---: | ---: |
| VGG-16, batch 64 | 57.98 images/s | 77th |
| VGG-16, batch 128 | 58.56 images/s | 77th |
| AlexNet, batch 64 | 1,091.67 images/s | 83rd |
| AlexNet, batch 128 | 1,162.65 images/s | 83rd |
| GoogLeNet, batch 64 | 499.89 images/s | 83rd |
| GoogLeNet, batch 128 | 516.44 images/s | 83rd |
| ResNet-50, batch 64 | 177.11 images/s | 90th |
| ResNet-50, batch 128 | 183.29 images/s | 90th |

Comparison labels shown by OpenBenchmarking:

| Model / Batch | 9470C | Threadripper 9980X | Threadripper 7980X | Ryzen 9 9950X | 2 x EPYC 9655 |
| --- | ---: | ---: | ---: | ---: | ---: |
| VGG-16, batch 64 | 57.98 | 85 | 52.47 | 25.81 | 207 |
| VGG-16, batch 128 | 58.56 | 88 | n/a | 26.79 | 212 |
| AlexNet, batch 64 | 1,091.67 | n/a | 732 | n/a | 2,182 |
| AlexNet, batch 128 | 1,162.65 | n/a | 911 | n/a | 3,015 |
| GoogLeNet, batch 64 | 499.89 | n/a | 261 | n/a | 798 |
| GoogLeNet, batch 128 | 516.44 | n/a | 290 | n/a | 1,030 |
| ResNet-50, batch 64 | 177.11 | 116 | 78 | n/a | 277 |
| ResNet-50, batch 128 | 183.29 | 125 | 83 | n/a | 326 |

Interpretation: TensorFlow CPU is a strong result for the 9470C. ResNet-50 lands in the 90th percentile and clearly beats Threadripper 7980X/9980X and desktop references shown in the comparison output. AlexNet and GoogLeNet are also strong at the 83rd percentile. VGG-16 is weaker at the 77th percentile but still beats Threadripper 7980X and Ryzen 9 9950X in the shown output. The ceiling is still below modern dual-socket EPYC 9655, but this benchmark confirms that CPU deep-learning inference is one of the platform's better real workloads.

### SVT-AV1 4.0

Result URL: https://openbenchmarking.org/result/2606031-NE-AV19470C958

Configuration:
- Profile: `pts/svt-av1-2.17.0`
- Presets: `13 (Fastest)`, `8`, `5 (Mid-Speed)`
- Inputs: `Bosphorus 4K`, `Bosphorus 1080p`, `Beauty 4K 10-bit`
- Mode: CPU only, default thread scaling (104 threads)

| Subtest | 9470C | Percentile |
| --- | ---: | ---: |
| Preset 5 - Bosphorus 4K | 46.572 FPS | 41st |
| Preset 8 - Bosphorus 4K | 121.403 FPS | 40th |
| Preset 13 - Bosphorus 4K | 226.554 FPS | 43rd |
| Preset 5 - Bosphorus 1080p | 135.799 FPS | 64th |
| Preset 8 - Bosphorus 1080p | 321.494 FPS | 61st |
| Preset 13 - Bosphorus 1080p | 682.139 FPS | 61st |
| Preset 5 - Beauty 4K 10-bit | 7.853 FPS | 32nd |
| Preset 8 - Beauty 4K 10-bit | 10.426 FPS | 23rd |
| Preset 13 - Beauty 4K 10-bit | 12.113 FPS | 22nd |

Interpretation: SVT-AV1 performance on the 9470C is moderate and varies by workload density. For lighter 1080p encoding (where core scaling works well and data fits easily in caches), the 9470C lands in the 61st-64th percentiles. However, for heavier 4K workloads and especially the demanding 10-bit Beauty test, performance drops to the 22nd-43rd percentiles. The processor's relatively low clock speed (3.5 GHz max boost) limits overall throughput in heavy CPU-bound encoding loops compared to high-frequency modern desktop and EPYC server CPUs.

## Notable Comparison Points

These values appeared in the OpenBenchmarking comparison output captured during the runs.

### 7-Zip

| Benchmark | EPYC 9755 | TR 9980X |
| --- | ---: | ---: |
| Compression | 1,123,940 MIPS | ~428,047 MIPS |
| Decompression | 831,688 MIPS | ~513,073 MIPS |

### oneDNN

| Benchmark | 9470C | EPYC 9755 | TR 9980X | 2 x EPYC 9475F | 2 x EPYC 9455 |
| --- | ---: | ---: | ---: | ---: | ---: |
| BF16 Conv | 44,155 | n/a | 22,383 | 34,979 | 32,464 |
| INT8 Conv | 105,713 | 53,335 | 41,748 | 64,073 | 59,409 |

### OpenVINO Throughput

| Benchmark | 9470C | EPYC 9755 | 2 x EPYC 9755 | 2 x EPYC 9655 | 2 x Xeon 6980P |
| --- | ---: | ---: | ---: | ---: | ---: |
| Face Detection FP16-INT8 | 208 FPS | ~193 FPS | 410 FPS | 312 FPS | 867 FPS |
| Vehicle Detection FP16-INT8 | 3,285 FPS | 10,894 FPS | 19,694 FPS | 14,655 FPS | 13,534 FPS |
| Road Segmentation ADAS FP16-INT8 | 900 FPS | 3,362 FPS | 6,931 FPS | 5,117 FPS | 4,406 FPS |

### llama.cpp

| Benchmark | 9470C | Threadripper 7980X | 2 x EPYC 9275F | 2 x EPYC 9475F | 2 x EPYC 9565 |
| --- | ---: | ---: | ---: | ---: | ---: |
| granite 3B Prompt Processing 2048 | 239.83 tok/s | 412 tok/s | 447 tok/s | 573 tok/s | 654 tok/s |

### vLLM CPU

| Benchmark | 9470C | EPYC 9755 | EPYC 9745 | EPYC 9655P | Threadripper 7980X | Ryzen 9 9950X3D |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Hermes 3B Average Latency | 4.10 s | 5.53 s | n/a | n/a | 9.93 s | 15.6 s |
| Hermes 3B Throughput | 235.14 tok/s | 392 tok/s | 371 tok/s | 339 tok/s | n/a | n/a |

### OpenVINO GenAI

| Benchmark | 9470C | EPYC 9755 | EPYC 9745 | Threadripper 7980X | Ryzen 9 9950X |
| --- | ---: | ---: | ---: | ---: | ---: |
| Qwen3-8B CPU | 25.46 tok/s | 24.99 tok/s | 21.79 tok/s | 15.02 tok/s | 5.90 tok/s |
| Qwen2.5-1.5B CPU | 63.72 tok/s | 61.10 tok/s | 51.95 tok/s | 54.65 tok/s | 26.65 tok/s |
| granite-3.0-8b CPU | 19.97 tok/s | 24.05 tok/s | 21.03 tok/s | 13.95 tok/s | 5.51 tok/s |
| Qwen3-8B TTFT | 74.01 ms | 50.33 ms | 56.49 ms | 78.15 ms | 178.00 ms |
| Qwen2.5-1.5B TTFT | 35.61 ms | 23.47 ms | 26.60 ms | 25.78 ms | 43.69 ms |
| granite-3.0-8b TTFT | 83.36 ms | 54.33 ms | 60.02 ms | 86.94 ms | 190.91 ms |

### Molecular Dynamics

| Benchmark | 9470C | EPYC 9755 | 2 x EPYC 9755 | 2 x EPYC 9965 | 2 x Xeon 6980P |
| --- | ---: | ---: | ---: | ---: | ---: |
| GROMACS water_GMX50 | 7.796 ns/day | n/a | 39.52 ns/day | 38.1 ns/day | 35.42 ns/day |
| LAMMPS 20k Atoms | 25.818 ns/day | 82 ns/day | n/a | 125 ns/day | 95 ns/day |
| CP2K H20-64 | 38.253 s | n/a | 14.119 s | 21.35 s | n/a |
| CP2K H20-256 | 306.749 s | n/a | n/a | n/a | 80 s |

### QuantLib

| Benchmark | 9470C | 2 x EPYC 9755 | 2 x Xeon 6980P | 2 x EPYC 9655 | 2 x EPYC 9555 |
| --- | ---: | ---: | ---: | ---: | ---: |
| Size S | 26.842 tasks/s | 198 tasks/s | 161 tasks/s | 139 tasks/s | 116 tasks/s |

### Linux Kernel Compile

| Benchmark | 9470C | EPYC 9575F | EPYC 8324P | EPYC 8224P | Ryzen AI 9 365 |
| --- | ---: | ---: | ---: | ---: | ---: |
| allmodconfig | 506.062 s | 257 s | 705 s | 966 s | 2118 s |

### FFTW

| Benchmark | 9470C | Ryzen 9 7950X | Core i9-14900K | Core i5-12600K | Xeon Gold 6414U |
| --- | ---: | ---: | ---: | ---: | ---: |
| Float+SSE 1D 4096 | 65,223 Mflops | 97,828 Mflops | 83,438 Mflops | 78,169 Mflops | 63,218 Mflops |

### y-cruncher

| Benchmark | 9470C | 2 x Xeon 6980P | 2 x EPYC 9745 | Threadripper 7980X | Ryzen 9 7950X3D |
| --- | ---: | ---: | ---: | ---: | ---: |
| Pi Digits 1B | 7.605 s | 2.859 s | 5.559 s | 10.911 s | 15.8 s |

### NumPy

| Benchmark | 9470C | EPYC 4585PX | EPYC 4245P | 2 x EPYC 9575F | Ryzen 7 7800X3D | Core i9-9900KS |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Score (single-threaded) | 472 | 1,098 | 1,067 | 982 | 785 | 447 |

### PyTorch CPU

#### ResNet-50 (batches/sec, More Is Better)

| Mode | 9470C | Ryzen 7 9800X3D | Ryzen 9 9950X | Ryzen 9 9950X3D | Core Ultra 9 285K | Threadripper 9980X | EPYC 9455P |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Batch Size: 1 | **247.14** | 140.00 | 132.00 | 125.00 | 116.00 | 91.00 | n/a |
| Batch Size: 64 | **153.61** | n/a | 52.50 | n/a | n/a | 64.40 | 71.12 |
| Batch Size: 512 | **153.24** | n/a | 52.10 | 77.46 | 73.64 | 63.80 | 69.88 |

#### ResNet-152 (batches/sec, More Is Better)

| Mode | 9470C | Core Ultra 7 270K+ | Ryzen 9 9950X3D | Ryzen 9 9900X3D | Ryzen 9 9950X | Core Ultra 9 285K | EPYC 9455P |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Batch Size: 1 | **86.82** | 44.37 | 39.04 | 37.35 | 38.50 | 35.60 | n/a |
| Batch Size: 64 | **59.17** | 26.50 | 28.13 | n/a | 18.90 | n/a | 25.80 |
| Batch Size: 512 | **58.84** | 26.80 | 28.42 | n/a | 19.10 | n/a | 26.10 |

#### EfficientNet-v2-l (batches/sec, More Is Better)

| Mode | 9470C | Ryzen 9 9950X3D | Ryzen 9 9900X3D | Core Ultra 7 270K+ | Ryzen 9 9950X | Core Ultra 9 285K | EPYC 9455P |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Batch Size: 1 | **55.48** | 24.50 | 22.44 | 21.80 | 23.20 | 18.90 | n/a |
| Batch Size: 64 | **37.57** | 15.88 | n/a | 14.50 | 10.50 | n/a | 14.20 |
| Batch Size: 512 | **37.76** | 16.10 | n/a | 18.42 | 10.70 | n/a | 14.50 |


### TensorFlow CPU

| Benchmark | 9470C | Threadripper 9980X | Threadripper 7980X | Ryzen 9 9950X | 2 x EPYC 9655 |
| --- | ---: | ---: | ---: | ---: | ---: |
| VGG-16 bs=64 | 57.98 img/s | 85 | 52.47 | 25.81 | 207 |
| VGG-16 bs=128 | 58.56 img/s | 88 | n/a | 26.79 | 212 |
| AlexNet bs=64 | 1,091.67 img/s | n/a | 732 | n/a | 2,182 |
| AlexNet bs=128 | 1,162.65 img/s | n/a | 911 | n/a | 3,015 |
| GoogLeNet bs=64 | 499.89 img/s | n/a | 261 | n/a | 798 |
| GoogLeNet bs=128 | 516.44 img/s | n/a | 290 | n/a | 1,030 |
| ResNet-50 bs=64 img/s | 177.11 | 116 | 78 | n/a | 277 |
| ResNet-50 bs=128 img/s | 183.29 | 125 | 83 | n/a | 326 |

### SVT-AV1

| Subtest | 9470C | 2 x EPYC 9755 | TR 9980X | R9 9950X3D | R9 9950X | Core Ultra 7 270K+ |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Preset 5 - Bosphorus 4K | 46.57 | 93.00 (2x) | 96.00 | 71.00 | 62.00 | 54.27 |
| Preset 8 - Bosphorus 4K | 121.40 | 234.00 (1x) | n/a | 170.00 | n/a | 157.00 |
| Preset 13 - Bosphorus 4K | 226.55 | n/a | n/a | 281.00 | n/a | 144.00 (10980XE) |
| Preset 5 - Bosphorus 1080p | 135.80 | 266.00 (2x) | 258.00 | 158.00 (9850X3D) | 221.00 | 145.00 (14900K) |
| Preset 8 - Bosphorus 1080p | 321.49 | 607.00 (2x) | n/a | 594.00 | 440.00 | 336.00 (14900K) |
| Preset 13 - Bosphorus 1080p | 682.14 | 1356.00 (2x) | 1264.00 | n/a | 794.00 | 761.00 (Ultra 5) |
| Preset 5 - Beauty 4K 10-bit | 7.85 | n/a | n/a | 11.93 | n/a | 4.91 (10980XE) |
| Preset 8 - Beauty 4K 10-bit | 10.43 | 15.14 (1x) | n/a | 18.27 (9950X3D2) | 17.40 | 18.15 |
| Preset 13 - Beauty 4K 10-bit | 12.11 | 17.69 (1x) | n/a | 21.58 (9950X3D2) | 20.64 | 9.79 (Ultra X7) |

## Overall Read

The Xeon Max 9470C is a specialized platform:

- Excellent: HBM bandwidth, oneDNN BF16, oneDNN INT8, PyTorch CPU (all OpenBenchmarking highs, 2.0-2.5x desktop), TensorFlow CPU ResNet-50.
- Good/mixed: OpenVINO small INT8 inference, y-cruncher (77th percentile, beats 64C TR), FFTW Float+SSE 1D 4096 (88th percentile).
- Ordinary for its class: 7-Zip, llama.cpp CPU BLAS, OpenVINO complex-model throughput, CP2K, Linux kernel compile, QuantLib, SVT-AV1 (22nd-43rd percentile on 4K/Beauty, 61st-64th percentile on 1080p).
- Not meaningful: NumPy (forced single-threaded).

Best next benchmarks to characterize the platform:

```bash
phoronix-test-suite benchmark pts/openvino-genai
```

HPCG was attempted with `192 192 192` and a 60 second runtime, but the system hard-locked before any score was written. GROMACS and LAMMPS completed successfully and were uploaded.

Additional benchmark candidates:

| Priority | Test | Status / why it is useful for 9470C |
| --- | --- | --- |
| 1 | `pts/hpcg` | Attempted; hard lock with `192^3`, no score. Retry only with smaller input or additional stability monitoring |
| 2 | `pts/gromacs` | Completed; real HPC molecular dynamics workload with broad OpenBenchmarking comparison data |
| 3 | `pts/lammps` | Completed; another HPC simulation workload useful against EPYC/server platforms |
| 4 | `pts/y-cruncher` | Completed; 77th percentile, 7.605 s @ 1B. Good AVX-512 + memory bandwidth showcase |
| 5 | `pts/openvino-genai` | Intel inference stack for generative AI; more relevant to CPU AI than llama.cpp BLAS |
| 6 | `pts/numpy` | Completed; 56th percentile, 472 score. Forced single-threaded — not a meaningful platform benchmark |
| 7 | `pts/pytorch` or `pts/intel-tensorflow` | Completed; PyTorch CPU all OpenBenchmarking highs, 2.0-2.5x best desktop CPUs |
| 8 | `pts/vllm` | GPU vLLM benchmark for RTX 3090; use separately from CPU vLLM results |
| 9 | pts/svt-av1 | Completed; SVT-AV1 2.17.0 video encoding. 22nd-43rd percentile on 4K/Beauty, 61st-64th percentile on 1080p |

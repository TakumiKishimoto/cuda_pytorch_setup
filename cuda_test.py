import torch
import sys
import subprocess

# Pythonのバージョンを表示
print("Python Version:", sys.version)

# PyTorchのバージョンを表示
print("PyTorch Version:", torch.__version__)

# CUDAのバージョンを表示
print("CUDA Version:", torch.version.cuda)

# CUDAが利用可能かどうかを確認
cuda_available = torch.cuda.is_available()
print("CUDA Available:", cuda_available)

# cuDNNのバージョンを表示
print("cuDNN Version:", torch.backends.cudnn.version())

# 利用可能なGPUの数を表示
gpu_count = torch.cuda.device_count()
print("Number of GPUs Available:", gpu_count)

# GPUの情報を表示
if cuda_available and gpu_count > 0:
    for i in range(gpu_count):
        print(f"GPU {i}: {torch.cuda.get_device_name(i)}")
        print(f"  - Memory Allocated: {torch.cuda.memory_allocated(i) / (1024**3):.2f} GB")
        print(f"  - Memory Cached: {torch.cuda.memory_reserved(i) / (1024**3):.2f} GB")
        print(f"  - Memory Total: {torch.cuda.get_device_properties(i).total_memory / (1024**3):.2f} GB")
else:
    print("No GPUs available or CUDA is not enabled")

# デバイスを設定
device = torch.device("cuda" if cuda_available else "cpu")
print("Using device:", device)

# フラグを初期化
allocation_test_ok = False
computation_test_ok = False

# 配置テスト
print("\n--- Tensor Allocation Test ---")
try:
    # GPU上にテンソルを配置
    x = torch.randn((1000, 1000), device=device)  # ランダムなテンソルを生成
    print("Tensor Allocation Test: OK")
    allocation_test_ok = True
except Exception as e:
    print("Tensor Allocation Test: Failed")
    print("Error during tensor allocation:", e)

# 計算テスト
print("\n--- Computation Test ---")
try:
    if allocation_test_ok:  # 配置が成功している場合のみ計算を実行
        y = torch.randn((1000, 1000), device=device)
        result = torch.matmul(x, y)  # 行列積を計算
        print("Computation Test: OK")
        computation_test_ok = True
    else:
        print("Computation Test: Skipped (Allocation Test failed)")
except Exception as e:
    print("Computation Test: Failed")
    print("Error during computation:", e)

# テストの総合結果
if allocation_test_ok and computation_test_ok:
    print("\nAll tests passed! Let's start coding!")
else:
    print("\nOne or more tests failed. Please check the errors above.")

print("*" * 50)
print("以下Additional Information:errorでも動きます")
# CUDAドライバとツールキットのバージョンを表示
try:
    driver_version = subprocess.check_output(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"]).decode("utf-8").strip()
    print("CUDA Driver Version:", driver_version)
except Exception as e:
    print("Error getting CUDA Driver Version:", e)

try:
    toolkit_version = subprocess.check_output(["nvcc", "--version"]).decode("utf-8")
    print("CUDA Toolkit Version:", toolkit_version)
except Exception as e:
    print("Error getting CUDA Toolkit Version:", e)

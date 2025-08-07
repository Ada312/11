import torch
from d2l import torch as d2l

print("PyTorch 版本:", torch.__version__)
print("CUDA 是否可用:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("使用 GPU:", torch.cuda.get_device_name(0))
else:
    print("当前使用 CPU 运行")

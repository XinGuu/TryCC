import torch
import os

os.system("hostname")
a = torch.rand((2, 3))
a = torch.rand((2, 3), device="cuda")
print(a)
import subprocess

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/pidigits/C/pidigitsC 10000 > /dev/null) 2>> /workspaces/Rusty-Kernels-Code/pidigits/C/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/pidigits/C/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/pidigits/C/pidigitsC 10000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/pidigits/C++/pidigitsC++ 10000 /dev/null) 2>> /workspaces/Rusty-Kernels-Code/pidigits/C++/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/pidigits/C++/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/pidigits/C++/pidigitsC++ 10000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call("time (/workspaces/Rusty-Kernels-Code/pidigits/Rust/target/release/Rust 10000 /dev/null) 2>> /workspaces/Rusty-Kernels-Code/pidigits/Rust/Results/time.txt", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)

for i in range(5):
    subprocess.call(f"valgrind --tool=massif --massif-out-file=\"/workspaces/Rusty-Kernels-Code/pidigits/Rust/Results/massif{i}.txt\" --pages-as-heap=yes /workspaces/Rusty-Kernels-Code/pidigits/Rust/target/release/Rust 10000 > /dev/null", shell=True, executable="/bin/bash", stdout=subprocess.PIPE)




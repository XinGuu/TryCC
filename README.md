# PyCharm + CC (GPU)

## CC
```
* https://ccdb.computecanada.ca/
* https://docs.alliancecan.ca/wiki/Getting_started
```
### Python
```
[name@server ~]$ module load python/3.10
[name@server ~]$ virtualenv --no-download ENV
[name@server ~]$ source ENV/bin/activate
[name@server ~]$ pip install --no-index --upgrade pip
(ENV) [name@server ~] pip install numpy --no-index
```


## SSH

### Tricks
* -N don't open terminal (just build the channel)

* -f run in background

## Practice
1. `Electerm` Quick commands (to salloc GPU) ---> get node name
2. `~/.ssh/config` change host name of Computenode
    ```
    # Jump box with public IP address
    Host Narval
        HostName narval.computecanada.ca
        User <username>
        IdentityFile ~/.ssh/id_rsa
    
    # Target machine with private IP address
    Host Computenode
        HostName [use cmd "hostname" to check]
        User <username>
        IdentityFile ~/.ssh/id_rsa
        ProxyCommand ssh -q -W %h:%p Narval
   ```
3. Setup PyCharm Remote Interpreter (only the first time)
   * Host: Computenode
4. You can hit Run/Debug to run the code
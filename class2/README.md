# Buffer overflow example

_Adapted From <https://dhavalkapil.com/blogs/Buffer-Overflow-Exploit/>_

1. Run `make` in this folder (or use the pre-compiled `vuln` binary provided)
2. Run `objdump -d vuln > vuln.dump`
3. Open `vuln.dump` in a text editor and look for the address of `use`
4. Edit `payload.py` to add the address of `use` in little-endian format
5. Run `./payload.py | ./vuln` to get the exploit!


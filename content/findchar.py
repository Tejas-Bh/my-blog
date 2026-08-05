import os

content_dir = "."  # The folder where fsp looks for markdown files

if not os.path.exists(content_dir):
    print(f"Could not find {content_dir} folder. Make sure you run this from your root project directory.")
    exit()

print("Scanning content files for cp1252 incompatible bytes...")
found_any = False

for root, dirs, files in os.walk(content_dir):
    for file in files:
        if file.endswith('.md') or file.endswith('.html'):
            filepath = os.path.join(root, file)
            
            with open(filepath, 'rb') as f:
                content = f.read()
                
            # Look for the byte 0x90 (144 in decimal)
            if b'\x90' in content:
                found_any = True
                position = content.find(b'\x90')
                print(f"\n[!] Found bad byte (0x90) in: {filepath}")
                print(f"    Byte position: {position}")
                
                # Extract surrounding context (30 bytes before and after)
                start = max(0, position - 30)
                end = min(len(content), position + 30)
                snippet = content[start:end]
                
                print(f"    Surrounding raw bytes: {snippet}")
                print(f"    Approximate text context: {snippet.decode('utf-8', errors='replace')}")

if not found_any:
    print("No 0x90 bytes found in the content directory. Check your config.toml or template files next!")

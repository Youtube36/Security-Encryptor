import base64
from PIL import Image

class SecurityEngine:
    SIGNATURE = "encrizh" # Kod unik anda

    @staticmethod
    def base64_encode(text):
        # Tambah signature sebelum encode
        signed_text = f"{SecurityEngine.SIGNATURE}:{text}"
        return base64.b64encode(signed_text.encode()).decode()

    @staticmethod
    def base64_decode(text):
        try:
            decoded = base64.b64decode(text).decode()
            if decoded.startswith(f"{SecurityEngine.SIGNATURE}:"):
                return decoded.replace(f"{SecurityEngine.SIGNATURE}:", "")
            return "Ralat: Tandatangan digital 'encrizh' tidak ditemui!"
        except:
            return "Ralat: Format Base64 tidak sah!"

    @staticmethod
    def enigma_cipher(text, shift=3):
        res = ""
        for char in text:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                res += chr((ord(char) - start + shift) % 26 + start)
            else:
                res += char
        return res

    @staticmethod
    def stego_hide(img_path, message, output_path):
        temp_img = Image.open(img_path).convert('RGB')
        data = list(temp_img.getdata())
        clean_img = Image.new('RGB', temp_img.size)
        clean_img.putdata(data)
        
        # Masukkan signature dalam steganografi
        full_payload = f"{SecurityEngine.SIGNATURE}|{message}#####"
        binary_msg = ''.join(format(ord(i), '08b') for i in full_payload)
        
        pixels = clean_img.load()
        data_idx = 0
        width, height = clean_img.size
        for y in range(height):
            for x in range(width):
                if data_idx < len(binary_msg):
                    r, g, b = pixels[x, y]
                    new_r = (r & 254) | int(binary_msg[data_idx])
                    pixels[x, y] = (new_r, g, b)
                    data_idx += 1
        
        clean_img.save(output_path, "PNG")
        return True

    @staticmethod
    def stego_reveal(img_path):
        img = Image.open(img_path).convert('RGB')
        pixels = img.load()
        binary_data = ""
        for y in range(img.height):
            for x in range(img.width):
                r, g, b = pixels[x, y]
                binary_data += str(r & 1)

        all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        decoded = ""
        for byte in all_bytes:
            try:
                decoded += chr(int(byte, 2))
                if decoded.endswith("#####"):
                    raw = decoded[:-5]
                    if raw.startswith(f"{SecurityEngine.SIGNATURE}|"):
                        return raw.replace(f"{SecurityEngine.SIGNATURE}|", "")
                    return "Amaran: Imej ini tidak mempunyai pengesahan 'encrizh'!"
            except: continue
        return "Tiada mesej ditemui."
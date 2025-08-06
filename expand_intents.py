# BULK EXPANSION SCRIPT
# Script untuk menambah banyak patterns dan responses sekaligus

import json
import os

def expand_all_intent_files():
    """
    Menambahkan lebih banyak short patterns dan responses ke semua file
    """
    
    # Short patterns yang umum digunakan mahasiswa
    common_short_patterns = [
        "apa", "gimana", "cara", "dimana", "kapan", "berapa", "siapa", "kenapa",
        "what", "how", "where", "when", "who", "why", "which", "can",
        "bisa", "mau", "butuh", "perlu", "ada", "minta", "tanya", "cari",
        "info", "informasi", "help", "bantuan", "tolong", "dong", "nih", "ya",
        "ok", "oke", "thanks", "makasih", "terima kasih", "thank you"
    ]
    
    # Common academic keywords
    academic_keywords = [
        "kuliah", "kampus", "academic", "akademik", "mahasiswa", "student",
        "semester", "sks", "mata kuliah", "course", "kelas", "class",
        "nilai", "grade", "ipk", "gpa", "ujian", "exam", "tugas", "assignment",
        "jadwal", "schedule", "daftar", "register", "bayar", "payment"
    ]
    
    print("🚀 Expanding all intent files with short patterns...")
    
    # Expand each file
    files_to_expand = [
        'intents_courses.json',
        'intents_grades.json', 
        'intents_finance.json',
        'intents_campus.json',
        'intents_graduation.json',
        'intents_closing.json'
    ]
    
    for filename in files_to_expand:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            # Add short patterns to each intent
            for intent in data['intents']:
                current_patterns = len(intent['patterns'])
                current_responses = len(intent['responses'])
                
                # Add relevant short patterns based on intent tag
                if 'course' in intent['tag']:
                    intent['patterns'].extend([
                        "jadwal", "schedule", "mata kuliah", "course", "kelas", "class",
                        "daftar kuliah", "registration", "ambil matakuliah", "enroll"
                    ])
                elif 'grade' in intent['tag']:
                    intent['patterns'].extend([
                        "nilai", "grade", "ipk", "gpa", "transkrip", "transcript",
                        "cek nilai", "lihat nilai", "hasil ujian", "score"
                    ])
                elif 'finance' in intent['tag'] or 'tuition' in intent['tag']:
                    intent['patterns'].extend([
                        "bayar", "payment", "spp", "tuition", "biaya", "fee",
                        "beasiswa", "scholarship", "cicilan", "installment"
                    ])
                elif 'campus' in intent['tag']:
                    intent['patterns'].extend([
                        "kampus", "campus", "fasilitas", "facility", "layanan", "service",
                        "wifi", "parkir", "kantin", "library", "perpustakaan"
                    ])
                elif 'graduation' in intent['tag']:
                    intent['patterns'].extend([
                        "lulus", "graduation", "wisuda", "skripsi", "thesis",
                        "syarat lulus", "requirements", "cumlaude"
                    ])
                elif 'goodbye' in intent['tag'] or 'thanks' in intent['tag']:
                    intent['patterns'].extend([
                        "bye", "goodbye", "sampai jumpa", "see you", "thanks",
                        "makasih", "terima kasih", "thank you", "thx"
                    ])
                
                # Add more generic responses
                base_responses = intent['responses'][:5]  # Take first 5 as base
                for i, response in enumerate(base_responses):
                    # Create variations
                    if i < 3:  # Add variations for first 3 responses
                        intent['responses'].append(f"Sure! {response}")
                        intent['responses'].append(f"Tentu! {response}")
                
                print(f"✅ {filename} - {intent['tag']}: {current_patterns} → {len(intent['patterns'])} patterns, {current_responses} → {len(intent['responses'])} responses")
            
            # Save expanded file
            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
    
    print("🎉 All files expanded!")

if __name__ == "__main__":
    expand_all_intent_files()

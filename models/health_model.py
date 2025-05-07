import pickle
import os
from typing import Dict, Any, List, Optional

class HealthAdvisorModel:
    """
    Model untuk memberikan rekomendasi kesehatan dan gizi.
    """
    def __init__(self, model_path: str = None):
        """
        Inisialisasi model.
        
        Args:
            model_path: Path ke file model (pickle/joblib) jika tersedia
        """
        self.model = None
        self.categories = [
            "riwayat_penyakit", 
            "gizi_mpasi_lansia", 
            "diet_hidup_sehat", 
            "tinggi_badan_otot", 
            "info_gizi_harian"
        ]
        
        # Load model jika tersedia
        if model_path and os.path.exists(model_path):
            try:
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
            except Exception as e:
                print(f"Error loading model: {e}")
    
    def predict(self, input_data: Dict[str, Any], category: str) -> Dict[str, Any]:
        """
        Melakukan prediksi berdasarkan input dan kategori.
        
        Args:
            input_data: Data input dari pengguna
            category: Kategori konsultasi
            
        Returns:
            Dict hasil prediksi dengan rekomendasi
        """
        # Validasi kategori
        if category not in self.categories:
            return {"error": "Kategori tidak valid"}
        
        # Fallback untuk mode tanpa model ML
        if self.model is None:
            return self._get_rule_based_recommendation(input_data, category)
        
        # Logika prediksi dengan model
        try:
            # Preprocessing dan prediksi
            # Implementasi sesuai model yang digunakan
            result = {
                "recommendation": "Rekomendasi berdasarkan model",
                "confidence": 0.85
            }
            return result
        except Exception as e:
            # Error handling
            print(f"Error in prediction: {e}")
            return {"error": str(e)}
    
    def _get_rule_based_recommendation(self, input_data: Dict[str, Any], category: str) -> Dict[str, Any]:
        """
        Memberikan rekomendasi berbasis aturan (fallback tanpa model ML).
        
        Args:
            input_data: Data input dari pengguna
            category: Kategori konsultasi
            
        Returns:
            Dict hasil rekomendasi
        """
        recommendations = {
            "riwayat_penyakit": {
                "jerawat": "Hindari makanan tinggi gula dan lemak. Konsumsi sayuran hijau, buah-buahan, dan air putih yang cukup.",
                "diabetes": "Batasi karbohidrat sederhana, konsumsi makanan berserat tinggi dan kontrol porsi makan."
            },
            "gizi_mpasi_lansia": {
                "mpasi": "Berikan makanan bertekstur lembut, kaya protein, zat besi, dan kalsium.",
                "lansia": "Fokus pada makanan tinggi serat, rendah garam, dan kaya kalsium serta vitamin D."
            },
            "diet_hidup_sehat": "Perbanyak konsumsi sayuran dan buah, batasi makanan olahan, dan jaga porsi makan.",
            "tinggi_badan_otot": "Konsumsi protein yang cukup (1.6-2g/kg berat badan), kalsium, dan vitamin D. Lakukan latihan beban.",
            "info_gizi_harian": "Kebutuhan kalori rata-rata: 2000-2500 kkal, protein 0.8g/kg berat badan, serat 25-30g/hari."
        }
        
        if category == "riwayat_penyakit" and "kondisi" in input_data:
            condition = input_data["kondisi"].lower()
            return {"recommendation": recommendations[category].get(
                condition, "Konsultasikan dengan dokter untuk kondisi spesifik ini."
            )}
        elif category == "gizi_mpasi_lansia" and "tipe" in input_data:
            tipe = input_data["tipe"].lower()
            return {"recommendation": recommendations[category].get(
                tipe, "Kebutuhan gizi perlu disesuaikan dengan kebutuhan individu."
            )}
        else:
            return {"recommendation": recommendations.get(
                category, "Masukkan lebih banyak detail untuk rekomendasi yang lebih spesifik."
            )}


# Contoh penggunaan
if __name__ == "__main__":
    # Inisialisasi model tanpa path (menggunakan rule-based)
    model = HealthAdvisorModel()
    
    # Contoh input untuk setiap kategori
    examples = [
        {
            "category": "riwayat_penyakit",
            "input": {"kondisi": "jerawat", "usia": 24, "durasi_kondisi": "3 bulan"}
        },
        {
            "category": "gizi_mpasi_lansia",
            "input": {"tipe": "mpasi", "usia_anak": 8, "status_kesehatan": "sehat"}
        },
        {
            "category": "diet_hidup_sehat",
            "input": {"tujuan_diet": "menurunkan berat badan", "berat_badan": 75, "tinggi_badan": 165, "aktivitas": "sedang"}
        },
        {
            "category": "tinggi_badan_otot",
            "input": {"usia": 19, "jenis_kelamin": "laki-laki", "aktivitas_fisik": "intensitas tinggi", "tujuan": "membangun otot"}
        },
        {
            "category": "info_gizi_harian",
            "input": {"usia": 35, "jenis_kelamin": "perempuan", "berat_badan": 60, "tinggi_badan": 160, "aktivitas": "rendah"}
        }
    ]
    
    # Cetak hasil prediksi untuk setiap contoh
    print("### Contoh Input dan Output untuk Model Health Advisor ###")
    for example in examples:
        category = example["category"]
        input_data = example["input"]
        
        print(f"\n*Input ({category}):*")
        print(f"json {input_data}")
        
        output = model.predict(input_data, category)
        print(f"*Output (rekomendasi):*")
        print(f"json {output}")
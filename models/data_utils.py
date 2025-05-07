# models/data_utils.py
from typing import Dict, Any, List, Optional

def validate_input(data: Dict[str, Any], category: str) -> Dict[str, Any]:
    """
    Memvalidasi input pengguna.
    
    Args:
        data: Data input dari form
        category: Kategori konsultasi
        
    Returns:
        Dict data yang sudah dibersihkan atau error
    """
    required_fields = {
        "riwayat_penyakit": ["kondisi", "lama_menderita"],
        "gizi_mpasi_lansia": ["tipe", "usia"],
        "diet_hidup_sehat": ["berat", "tinggi", "aktivitas"],
        "tinggi_badan_otot": ["usia", "tinggi", "berat", "target"],
        "info_gizi_harian": ["usia", "jenis_kelamin", "aktivitas"]
    }
    
    # Periksa kategori valid
    if category not in required_fields:
        return {"error": "Kategori tidak valid"}
    
    # Periksa field yang diperlukan
    missing_fields = [field for field in required_fields[category] if field not in data or not data[field]]
    if missing_fields:
        return {"error": f"Data tidak lengkap: {', '.join(missing_fields)}"}
    
    # Bersihkan data
    clean_data = {key: value.strip() if isinstance(value, str) else value 
                 for key, value in data.items()}
    
    return clean_data

def prepare_model_input(data: Dict[str, Any], category: str) -> Dict[str, Any]:
    """
    Menyiapkan data untuk input ke model.
    
    Args:
        data: Data dari form yang sudah divalidasi
        category: Kategori konsultasi
        
    Returns:
        Dict data yang siap untuk model
    """
    # Implementasi sesuai kebutuhan preprocessing model
    # Contoh sederhana: normalisasi nilai numerik
    if category in ["diet_hidup_sehat", "tinggi_badan_otot", "info_gizi_harian"]:
        if "berat" in data:
            data["berat"] = float(data["berat"])
        if "tinggi" in data:
            data["tinggi"] = float(data["tinggi"])
        if "usia" in data:
            data["usia"] = int(data["usia"])
    
    return data
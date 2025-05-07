# services/advisor.py
from models.health_model import HealthAdvisorModel
from models.data_utils import validate_input, prepare_model_input
from typing import Dict, Any, Optional

class HealthAdvisorService:
    """
    Layanan untuk memberikan saran kesehatan dan gizi.
    """
    def __init__(self, model_path: Optional[str] = None):
        """
        Inisialisasi layanan.
        
        Args:
            model_path: Path ke model ML jika ada
        """
        self.model = HealthAdvisorModel(model_path)
    
    def get_advice(self, form_data: Dict[str, Any], category: str) -> Dict[str, Any]:
        """
        Mendapatkan saran berdasarkan data dari form.
        
        Args:
            form_data: Data dari form web
            category: Kategori konsultasi
            
        Returns:
            Dict berisi saran atau error
        """
        # Validasi input
        validated_data = validate_input(form_data, category)
        if "error" in validated_data:
            return validated_data
        
        # Prepare data untuk model
        model_input = prepare_model_input(validated_data, category)
        
        # Dapatkan prediksi dari model
        prediction = self.model.predict(model_input, category)
        
        # Format hasil
        result = {
            "category": category,
            "input": validated_data,
            "recommendation": prediction.get("recommendation", ""),
            "error": prediction.get("error", None)
        }
        
        return result
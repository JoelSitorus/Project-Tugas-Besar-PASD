# routes/main.py
from flask import Blueprint, render_template, request, jsonify
from services.advisor import HealthAdvisorService
from config import Config

main_bp = Blueprint('main', __name__)
advisor_service = HealthAdvisorService(Config.MODEL_PATH)

@main_bp.route('/', methods=['GET'])
def index():
    """Halaman utama aplikasi."""
    return render_template('index.html')

@main_bp.route('/consult', methods=['POST'])
def consult():
    """
    Endpoint untuk mendapatkan saran kesehatan.
    """
    # Ambil data dari form
    data = request.form.to_dict()
    category = data.get('category')
    
    if not category:
        return render_template('result.html', error="Kategori tidak dipilih")
    
    # Proses melalui service
    result = advisor_service.get_advice(data, category)
    
    # Tampilkan error jika ada
    if "error" in result and result["error"]:
        return render_template('result.html', error=result["error"])
    
    # Tampilkan hasil
    return render_template('result.html', result=result)

@main_bp.route('/api/consult', methods=['POST'])
def api_consult():
    """
    API endpoint untuk mendapatkan saran kesehatan.
    """
    # Ambil data JSON
    data = request.get_json()
    if not data:
        return jsonify({"error": "Data tidak valid"}), 400
    
    category = data.get('category')
    if not category:
        return jsonify({"error": "Kategori tidak dipilih"}), 400
    
    # Proses melalui service
    result = advisor_service.get_advice(data, category)
    
    return jsonify(result)
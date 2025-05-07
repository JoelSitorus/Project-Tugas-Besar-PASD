// Menampilkan field sesuai kategori yang dipilih
function showFields() {
    // Sembunyikan semua field kategori
    const categoryFields = document.querySelectorAll('.category-fields');
    categoryFields.forEach(field => {
        field.style.display = 'none';
    });
    
    // Tampilkan field sesuai kategori yang dipilih
    const category = document.getElementById('category').value;
    if (category) {
        const selectedFields = document.getElementById(`fields_${category}`);
        if (selectedFields) {
            selectedFields.style.display = 'block';
        }
    }
}

// Initialize on page load
document.addEventListener('DOMContentLoaded', function() {
    showFields();
});
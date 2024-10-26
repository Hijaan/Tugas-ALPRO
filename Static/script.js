function scanProduct() {
    const barcode = document.getElementById('barcodeInput').value;
    fetch('/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ barcode: barcode }),
    })
    .then(response => response.json())
    .then(data => {
        if (data.price) {
            document.getElementById('result').innerText = `Harga: Rp ${data.price}`;
        } else {
            document.getElementById('result').innerText = 'Barang tidak ditemukan';
        }
    })
    .catch(error => {
        document.getElementById('result').innerText = 'Terjadi kesalahan';
        console.error('Error:', error);
    });
}

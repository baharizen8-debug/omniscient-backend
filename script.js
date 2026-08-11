async function fetchGoldData() {
    try {
        // Mengambil data dari backend sendiri
        const response = await fetch('/api/gold-data');
        const data = await response.json();
        
        document.getElementById('gold-price').innerText = `$${data.price}`;
        document.getElementById('market-status').innerText = data.status;
        
        if (data.status === 'Bullish') {
            document.getElementById('market-status').style.color = '#22c55e';
        } else {
            document.getElementById('market-status').style.color = '#ef4444';
        }
    } catch (error) {
        console.error('Gagal:', error);
    }
}

fetchGoldData();
setInterval(fetchGoldData, 30000);

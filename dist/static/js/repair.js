// JavaScript for device repair functionality

document.addEventListener('DOMContentLoaded', function() {
    // Set up event handlers for repair buttons
    setupRepairHandlers();
    
    // Initialize repair history
    loadRepairHistory();
    
    // Set up reset device button
    setupResetDevice();
});

// Setup repair button event handlers
function setupRepairHandlers() {
    document.querySelectorAll('.repair-btn').forEach(button => {
        button.addEventListener('click', function() {
            const repairType = this.dataset.repair;
            startRepair(repairType);
        });
    });
}

// Start the repair process
function startRepair(repairType) {
    // Get the repair option element
    const repairOption = document.getElementById(`${repairType === 'full' ? 'full-repair' : 
                                                 repairType === 'malware' ? 'clean-malware' : 
                                                 repairType === 'system' ? 'optimize-system' : 
                                                 'privacy-fix'}`);
    
    // Change the button to show progress
    const repairBtn = repairOption.querySelector('.repair-btn');
    const originalText = repairBtn.textContent;
    repairBtn.textContent = 'Memproses...';
    repairBtn.disabled = true;
    
    // Create a progress display
    const repairDetails = repairOption.querySelector('.repair-details');
    const progressElement = document.createElement('div');
    progressElement.className = 'repair-progress';
    progressElement.innerHTML = `
        <div class="spinner"></div>
        <p id="repair-status">Memulai perbaikan...</p>
        <div class="progress-container">
            <div id="repair-progress-bar" class="progress-bar" style="width: 0%"></div>
        </div>
        <div class="repair-log" id="repair-log"></div>
    `;
    
    // Insert after the button
    repairBtn.insertAdjacentElement('afterend', progressElement);
    
    // Simulate the repair process
    simulateRepair(repairType, repairBtn, originalText, progressElement);
}

// Simulate the repair process
function simulateRepair(repairType, button, originalText, progressElement) {
    const progressBar = progressElement.querySelector('#repair-progress-bar');
    const statusText = progressElement.querySelector('#repair-status');
    const repairLog = progressElement.querySelector('#repair-log');
    
    let progress = 0;
    let repairSteps = [];
    
    // Define steps based on repair type
    switch(repairType) {
        case 'malware':
            repairSteps = [
                "Memindai aplikasi berbahaya...",
                "Mengidentifikasi file yang terinfeksi...",
                "Menghapus file malware yang ditemukan...",
                "Membersihkan registry sistem...",
                "Memverifikasi pembersihan malware..."
            ];
            break;
        case 'system':
            repairSteps = [
                "Menganalisis pengaturan sistem...",
                "Mengoptimalkan file sistem...",
                "Memperbaiki pengaturan keamanan...",
                "Meningkatkan performa sistem...",
                "Menerapkan perubahan pengaturan..."
            ];
            break;
        case 'privacy':
            repairSteps = [
                "Mengaudit izin aplikasi...",
                "Mengidentifikasi masalah privasi...",
                "Memperbaiki kebocoran data...",
                "Mengatur ulang izin aplikasi...",
                "Memverifikasi perlindungan privasi..."
            ];
            break;
        case 'full':
            repairSteps = [
                "Memulai pemindaian menyeluruh...",
                "Menghapus aplikasi berbahaya dan malware...",
                "Mengoptimalkan pengaturan sistem...",
                "Memperbaiki masalah privasi dan keamanan...",
                "Finalisasi dan verifikasi perbaikan..."
            ];
            break;
    }
    
    // Add initial log entry
    addLogEntry(repairLog, "Memulai proses perbaikan...", "info");
    
    // Simulate progress
    const interval = setInterval(() => {
        progress += 4;
        progressBar.style.width = progress + '%';
        
        // Update status text at certain points
        if (progress % 20 === 0) {
            const stepIndex = Math.floor(progress / 20) - 1;
            if (stepIndex < repairSteps.length) {
                statusText.textContent = repairSteps[stepIndex];
                // Add log entry
                addLogEntry(repairLog, repairSteps[stepIndex], "info");
                
                // Simulate finding and fixing issues
                if (Math.random() > 0.5) {
                    setTimeout(() => {
                        const issue = getRandomIssue(repairType);
                        addLogEntry(repairLog, `Masalah ditemukan: ${issue}`, "warning");
                        
                        setTimeout(() => {
                            addLogEntry(repairLog, `Berhasil memperbaiki: ${issue}`, "success");
                        }, 800);
                    }, 500);
                }
            }
        }
        
        if (progress >= 100) {
            clearInterval(interval);
            statusText.textContent = "Perbaikan selesai!";
            addLogEntry(repairLog, "Perbaikan berhasil diselesaikan!", "success");
            
            // Re-enable the button after a delay
            setTimeout(() => {
                button.textContent = originalText;
                button.disabled = false;
                
                // Add a completion message and remove progress display
                const completionMessage = document.createElement('p');
                completionMessage.className = 'status-completed';
                completionMessage.innerHTML = `<i class="fas fa-check-circle"></i> Perbaikan berhasil dilakukan.`;
                progressElement.replaceWith(completionMessage);
                
                // Add to repair history
                addToRepairHistory(repairType);
            }, 1500);
        }
    }, 200);
}

// Add a log entry to the repair log
function addLogEntry(logElement, message, type) {
    const timestamp = new Date().toLocaleTimeString();
    const entry = document.createElement('div');
    entry.className = 'repair-log-entry';
    entry.innerHTML = `<span class="log-timestamp">[${timestamp}]</span> <span class="log-${type}">${message}</span>`;
    logElement.appendChild(entry);
    logElement.scrollTop = logElement.scrollHeight;
}

// Get a random issue message based on repair type
function getRandomIssue(repairType) {
    const issues = {
        'malware': [
            "Trojan terdeteksi di aplikasi 'Quick Calculator'",
            "Adware ditemukan di 'Free Flashlight App'",
            "Aplikasi mencurigakan mengakses lokasi di latar belakang",
            "File terinfeksi di folder unduhan",
            "Spyware memantau aktivitas pengguna"
        ],
        'system': [
            "USB Debugging aktif dan tidak aman",
            "Verifikasi aplikasi nonaktif",
            "Patch keamanan tertinggal 3 bulan",
            "Enkripsi perangkat tidak aktif",
            "Opsi pengembang diaktifkan dan berbahaya"
        ],
        'privacy': [
            "5 aplikasi memiliki akses lokasi yang tidak perlu",
            "Aplikasi 'Game Puzzle' mengakses kontak Anda",
            "Data pribadi disinkronkan ke server tidak aman",
            "3 aplikasi mengakses kamera saat tidak digunakan",
            "Riwayat pencarian disimpan dan tidak dilindungi"
        ],
        'full': [
            "Kerentanan sistem terdeteksi di pengaturan WiFi",
            "Aplikasi dengan rating buruk di toko aplikasi terinstal",
            "Konfigurasi DNS tidak aman",
            "Izin perangkat yang berlebihan diberikan ke app pihak ketiga",
            "Fungsionalitas kriptografi yang lemah digunakan oleh beberapa aplikasi"
        ]
    };
    
    const typeIssues = issues[repairType] || issues['full'];
    return typeIssues[Math.floor(Math.random() * typeIssues.length)];
}

// Load repair history from local storage
function loadRepairHistory() {
    const historyContainer = document.getElementById('repair-history');
    
    // Check if we have history in local storage
    const history = JSON.parse(localStorage.getItem('repairHistory') || '[]');
    
    if (history.length === 0) {
        historyContainer.innerHTML = '<p>Belum ada riwayat perbaikan.</p>';
        return;
    }
    
    // Display history
    let historyHTML = '';
    history.forEach(item => {
        historyHTML += `
            <div class="repair-history-item">
                <div><span class="repair-type">${getRepairTypeName(item.type)}</span></div>
                <div class="repair-timestamp">${new Date(item.timestamp).toLocaleString()}</div>
                <div class="repair-status status-completed">
                    <i class="fas fa-check-circle"></i> Selesai
                </div>
            </div>
        `;
    });
    
    historyContainer.innerHTML = historyHTML;
}

// Add a repair to the history
function addToRepairHistory(repairType) {
    const history = JSON.parse(localStorage.getItem('repairHistory') || '[]');
    
    // Add the new repair
    history.unshift({
        type: repairType,
        timestamp: new Date().toISOString()
    });
    
    // Limit history to 10 items
    if (history.length > 10) {
        history.pop();
    }
    
    // Save and reload
    localStorage.setItem('repairHistory', JSON.stringify(history));
    loadRepairHistory();
}

// Get human-readable name for repair type
function getRepairTypeName(type) {
    switch(type) {
        case 'malware': return 'Pembersihan Malware';
        case 'system': return 'Optimalisasi Sistem';
        case 'privacy': return 'Perbaikan Privasi';
        case 'full': return 'Perbaikan Menyeluruh';
        default: return 'Perbaikan';
    }
}

// Setup reset device button
function setupResetDevice() {
    const resetBtn = document.getElementById('resetDeviceBtn');
    if (resetBtn) {
        resetBtn.addEventListener('click', function() {
            if (confirm('PERINGATAN: Ini akan menghapus semua data pada perangkat Anda. Lanjutkan?')) {
                if (confirm('Apakah Anda yakin? Tindakan ini tidak dapat dibatalkan.')) {
                    // Simulate reset
                    document.body.innerHTML = `
                        <div style="text-align: center; padding: 2rem;">
                            <div class="spinner"></div>
                            <h2>Melakukan Reset Perangkat</h2>
                            <p>Perangkat Anda sedang dikembalikan ke pengaturan pabrik...</p>
                            <p>Jangan matikan atau restart perangkat Anda.</p>
                            <div class="progress-container">
                                <div id="reset-progress" class="progress-bar" style="width: 0%;"></div>
                            </div>
                        </div>
                    `;
                    
                    let progress = 0;
                    const interval = setInterval(() => {
                        progress += 1;
                        document.getElementById('reset-progress').style.width = progress + '%';
                        
                        if (progress >= 100) {
                            clearInterval(interval);
                            document.body.innerHTML = `
                                <div style="text-align: center; padding: 2rem;">
                                    <i class="fas fa-check-circle" style="font-size: 4rem; color: var(--secondary-color);"></i>
                                    <h2>Reset Selesai</h2>
                                    <p>Perangkat Anda telah berhasil dikembalikan ke pengaturan pabrik.</p>
                                    <p>Perangkat akan restart dalam beberapa detik.</p>
                                    <a href="/" class="btn">Kembali ke Beranda</a>
                                </div>
                            `;
                        }
                    }, 50);
                }
            }
        });
    }
}
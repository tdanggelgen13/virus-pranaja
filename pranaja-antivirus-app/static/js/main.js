// Main JavaScript for Android Security Scanner

document.addEventListener('DOMContentLoaded', function() {
    // Initialize theme toggles
    const cyberpunkToggle = document.getElementById('toggleCyberpunk');
    const safeModeToggle = document.getElementById('toggleSafeMode');
    
    if (cyberpunkToggle) {
        cyberpunkToggle.addEventListener('click', function() {
            document.body.classList.toggle('cyberpunk-mode');
            // Save preference to localStorage
            if (document.body.classList.contains('cyberpunk-mode')) {
                localStorage.setItem('theme', 'cyberpunk');
                // Ensure safe mode is turned off when cyberpunk is on
                document.body.classList.remove('safe-mode');
            } else {
                localStorage.setItem('theme', 'light');
            }
        });
    }
    
    if (safeModeToggle) {
        safeModeToggle.addEventListener('click', function() {
            document.body.classList.toggle('safe-mode');
            // Save preference to localStorage
            if (document.body.classList.contains('safe-mode')) {
                localStorage.setItem('safeMode', 'true');
                // Ensure cyberpunk mode is turned off when safe mode is on
                document.body.classList.remove('cyberpunk-mode');
                localStorage.setItem('theme', 'light');
            } else {
                localStorage.setItem('safeMode', 'false');
            }
        });
    }
    
    // Load saved preferences
    const savedTheme = localStorage.getItem('theme');
    const safeMode = localStorage.getItem('safeMode');
    
    if (savedTheme === 'cyberpunk') {
        document.body.classList.add('cyberpunk-mode');
    }
    
    if (safeMode === 'true') {
        document.body.classList.add('safe-mode');
    }
    
    // Initialize the application
    initApp();
    
    // Add event listeners
    setupEventListeners();
});

// Application initialization
function initApp() {
    // Check what page we're on and run appropriate initializations
    const currentPath = window.location.pathname;
    
    if (currentPath === '/' || currentPath === '/index.html') {
        // Home page initialization
        updateDeviceStatus();
    } else if (currentPath === '/scan_results') {
        // Scan results page initialization
        initScanResults();
    } else if (currentPath === '/device_status') {
        // Device status page initialization
        initDeviceStatus();
    } else if (currentPath === '/education') {
        // Education page initialization
        initEducationPage();
    }
}

// Set up event listeners
function setupEventListeners() {
    // Scan button
    const scanButton = document.getElementById('startScanBtn');
    if (scanButton) {
        scanButton.addEventListener('click', startScan);
    }
    
    // Cleanup buttons
    document.querySelectorAll('.cleanup-btn').forEach(button => {
        button.addEventListener('click', function(e) {
            const threatId = this.dataset.threatId;
            cleanupThreat(threatId);
        });
    });
    
    // Education topic items
    document.querySelectorAll('.topic-item').forEach(item => {
        item.addEventListener('click', function() {
            const topicId = this.dataset.topicId;
            loadTopicContent(topicId);
        });
    });
}

// Start a security scan
function startScan() {
    // Show scanning UI
    const scanSection = document.getElementById('scanSection');
    if (scanSection) {
        scanSection.innerHTML = `
            <div class="card">
                <div class="card-title">Scanning in progress</div>
                <div class="spinner"></div>
                <div id="scanStatus">Initializing scan...</div>
                <div class="progress-container">
                    <div id="scanProgress" class="progress-bar" style="width: 0%"></div>
                </div>
            </div>
        `;
    }
    
    // Simulate scanning progress
    simulateScanProgress();
    
    // Start actual scan
    fetch('/scan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        // After scan completes, redirect to results
        window.location.href = '/scan_results';
    })
    .catch(error => {
        console.error('Error during scan:', error);
        if (scanSection) {
            scanSection.innerHTML = `
                <div class="card">
                    <div class="card-title">Scan Failed</div>
                    <p>There was an error during the scan. Please try again.</p>
                    <button id="retryBtn" class="btn btn-full">Retry Scan</button>
                </div>
            `;
            document.getElementById('retryBtn').addEventListener('click', startScan);
        }
    });
}

// Simulate the scan progress for UI feedback
function simulateScanProgress() {
    const progressBar = document.getElementById('scanProgress');
    const statusText = document.getElementById('scanStatus');
    let progress = 0;
    
    const scanSteps = [
        "Checking installed applications...",
        "Analyzing app permissions...",
        "Scanning system settings...",
        "Checking network configuration...",
        "Analyzing storage security...",
        "Finalizing results..."
    ];
    
    const interval = setInterval(() => {
        progress += 5;
        if (progressBar) progressBar.style.width = progress + '%';
        
        // Update status text at certain points
        if (progress % 20 === 0 && statusText) {
            const stepIndex = Math.floor(progress / 20);
            if (stepIndex < scanSteps.length) {
                statusText.textContent = scanSteps[stepIndex];
            }
        }
        
        if (progress >= 100) {
            clearInterval(interval);
            if (statusText) statusText.textContent = "Scan complete! Processing results...";
        }
    }, 200);
}

// Initialize scan results page
function initScanResults() {
    // Add event listeners for cleanup buttons
    document.querySelectorAll('.cleanup-btn').forEach(button => {
        button.addEventListener('click', function() {
            const threatId = this.dataset.threatId;
            const threatItem = this.closest('.result-item');
            
            // Show cleaning animation
            this.textContent = "Cleaning...";
            this.disabled = true;
            
            cleanupThreat(threatId)
                .then(success => {
                    if (success) {
                        // Visual feedback of successful cleanup
                        setTimeout(() => {
                            threatItem.style.transition = "opacity 0.5s ease-out";
                            threatItem.style.opacity = "0";
                            setTimeout(() => {
                                threatItem.remove();
                                
                                // Check if there are no more threats
                                const remainingThreats = document.querySelectorAll('.result-item').length;
                                if (remainingThreats === 0) {
                                    document.getElementById('resultsContainer').innerHTML = `
                                        <div class="card">
                                            <div class="card-title">All Clear!</div>
                                            <p>All threats have been successfully removed from your device.</p>
                                            <button id="backToHomeBtn" class="btn btn-full">Back to Home</button>
                                        </div>
                                    `;
                                    document.getElementById('backToHomeBtn').addEventListener('click', () => {
                                        window.location.href = '/';
                                    });
                                }
                            }, 500);
                        }, 1000);
                    } else {
                        // Handle cleanup failure
                        this.textContent = "Cleanup failed";
                        this.classList.remove('btn-warning');
                        this.classList.add('btn-danger');
                        setTimeout(() => {
                            this.textContent = "Try Again";
                            this.disabled = false;
                        }, 1500);
                    }
                });
        });
    });
}

// Clean up a specific threat
function cleanupThreat(threatId) {
    return fetch('/cleanup', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `threat_id=${threatId}`
    })
    .then(response => response.json())
    .then(data => {
        return data.success;
    })
    .catch(error => {
        console.error('Error during cleanup:', error);
        return false;
    });
}

// Initialize device status page
function initDeviceStatus() {
    updateDeviceStatus();
    
    // Set up recommendations
    document.querySelectorAll('.recommendation-item').forEach(item => {
        const expandBtn = item.querySelector('.expand-btn');
        if (expandBtn) {
            expandBtn.addEventListener('click', function() {
                const details = item.querySelector('.recommendation-details');
                if (details) {
                    details.classList.toggle('expanded');
                    this.textContent = details.classList.contains('expanded') ? 'Less' : 'More';
                }
            });
        }
    });
}

// Update device security status display
function updateDeviceStatus() {
    const statusContainer = document.getElementById('deviceStatusContainer');
    if (!statusContainer) return;
    
    fetch('/device_status')
        .then(response => response.json())
        .then(data => {
            // Update the UI with the status data
            updateSecurityScore(data.security_score);
        })
        .catch(error => {
            console.error('Error fetching device status:', error);
            if (statusContainer) {
                statusContainer.innerHTML = `
                    <div class="card">
                        <div class="card-title">Status Unavailable</div>
                        <p>Unable to retrieve device security status. Please try again later.</p>
                        <button id="retryStatusBtn" class="btn btn-full">Retry</button>
                    </div>
                `;
                document.getElementById('retryStatusBtn').addEventListener('click', updateDeviceStatus);
            }
        });
}

// Update the security score display
function updateSecurityScore(score) {
    const scoreCircle = document.getElementById('securityScore');
    if (scoreCircle) {
        // Update the score text
        scoreCircle.textContent = score;
        
        // Update the circle gradient based on score
        const scoreContainer = document.querySelector('.score-circle');
        if (scoreContainer) {
            let color;
            if (score >= 80) {
                color = 'var(--secondary-color)'; // Good
            } else if (score >= 60) {
                color = 'var(--warning-color)'; // Warning
            } else {
                color = 'var(--danger-color)'; // Danger
            }
            
            scoreContainer.style.background = `conic-gradient(
                ${color} 0%, 
                ${color} ${score}%, 
                #e0e0e0 ${score}%, 
                #e0e0e0 100%
            )`;
        }
    }
}

// Initialize the education page
function initEducationPage() {
    // Topic click handlers are added in setupEventListeners
}

// Load topic content 
function loadTopicContent(topicId) {
    fetch(`/education/${topicId}`)
        .then(response => response.json())
        .then(data => {
            const contentContainer = document.getElementById('educationContent');
            if (contentContainer) {
                // Generate HTML for the article
                let sectionsHtml = '';
                data.sections.forEach(section => {
                    sectionsHtml += `
                        <h3>${section.heading}</h3>
                        <div class="section-content">${formatContent(section.content)}</div>
                    `;
                });
                
                contentContainer.innerHTML = `
                    <div class="article-header">
                        <button id="backToTopicsBtn" class="btn">← Back to Topics</button>
                        <h2>${data.title}</h2>
                    </div>
                    <div class="article-content">
                        ${sectionsHtml}
                    </div>
                `;
                
                // Add back button handler
                document.getElementById('backToTopicsBtn').addEventListener('click', () => {
                    // Show topics list again
                    document.getElementById('topicsList').style.display = 'block';
                    contentContainer.innerHTML = '';
                });
                
                // Hide the topics list
                document.getElementById('topicsList').style.display = 'none';
            }
        })
        .catch(error => {
            console.error('Error loading topic:', error);
        });
}

// Format content text with markdown-like syntax
function formatContent(content) {
    // Convert the content string to HTML
    // This handles basic formatting like bold, lists, etc.
    let formatted = content
        // Preserve line breaks
        .replace(/\n\n/g, '<br><br>')
        // Bold text
        .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
        // Italic text
        .replace(/\*(.*?)\*/g, '<em>$1</em>')
        // Convert lists (simple version)
        .replace(/- (.*?)(\n|$)/g, '<li>$1</li>')
        // Add line breaks
        .replace(/\n/g, '<br>');
    
    // Wrap lists in ul tags - this is a simple approach
    if (formatted.includes('<li>')) {
        formatted = formatted.replace(/<br><li>/g, '<li>');
        formatted = '<ul>' + formatted + '</ul>';
        formatted = formatted.replace(/<ul><br>/g, '<ul>');
        formatted = formatted.replace(/<br><\/ul>/g, '</ul>');
    }
    
    return formatted;
}

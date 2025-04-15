import os
import json
import time
import random
from datetime import datetime

# Store last scan results and logs
_last_scan_results = None
_activity_logs = []
_firewall_blocks = []
_realtime_scan_active = False

def scan_device():
    """
    Perform a security scan on the device.
    
    In a real app, this would use Android APIs to check for:
    - Installed apps and their permissions
    - System settings
    - Network configuration
    - Malicious files
    
    For this simulation, we're generating representative results.
    """
    global _last_scan_results
    
    # Simulate scanning time
    time.sleep(2)
    
    # Create scan results structure
    scan_results = {
        "scan_id": str(int(time.time())),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "threats_found": [],
        "system_status": {
            "os_version": "Android 11",
            "security_patch": "2023-05-01",
            "encryption": "Enabled",
            "unknown_sources": "Disabled",
            "developer_options": "Disabled",
            "usb_debugging": "Disabled"
        },
        "scan_details": {
            "apps_scanned": 45,
            "files_scanned": 1204,
            "settings_checked": 12
        }
    }
    
    # Generate potential threats based on security checks
    # These would be real threats found in a real app
    potential_threats = [
        {
            "id": "threat-001",
            "type": "suspicious_app",
            "name": "Unknown File Manager",
            "description": "This app requests excessive permissions that could compromise your privacy.",
            "risk_level": "medium",
            "cleanup_action": "uninstall_app"
        },
        {
            "id": "threat-002",
            "type": "system_setting",
            "name": "USB Debugging",
            "description": "USB Debugging is enabled, which can allow unauthorized access to your device when connected to a computer.",
            "risk_level": "low",
            "cleanup_action": "disable_setting"
        },
        {
            "id": "threat-003",
            "type": "network_vulnerability",
            "name": "Insecure WiFi",
            "description": "Your device is connected to an unsecured WiFi network.",
            "risk_level": "high",
            "cleanup_action": "disconnect_network"
        },
        {
            "id": "threat-004",
            "type": "permission_abuse",
            "name": "Location Tracking",
            "description": "Multiple apps are tracking your location in the background.",
            "risk_level": "medium",
            "cleanup_action": "review_permissions"
        }
    ]
    
    # Randomly select 0-3 threats to report
    num_threats = random.randint(0, 3)
    if num_threats > 0:
        scan_results["threats_found"] = random.sample(potential_threats, num_threats)
    
    _last_scan_results = scan_results
    return scan_results

def get_last_scan_results():
    """
    Return the results of the last scan.
    
    Returns:
        dict: The results of the last scan, or None if no scan has been performed.
    """
    global _last_scan_results
    if not _last_scan_results:
        _last_scan_results = scan_device()  # Perform a scan if none exists
    return _last_scan_results

def clean_threat(threat_id):
    """
    Clean up a detected threat.
    
    In a real app, this would take action based on the threat type.
    For this simulation, we're just pretending to clean it.
    
    Args:
        threat_id (str): The ID of the threat to clean.
        
    Returns:
        bool: True if cleanup was successful, False otherwise.
    """
    global _last_scan_results
    
    if not _last_scan_results:
        return False
    
    # Find the threat in the last scan results
    for i, threat in enumerate(_last_scan_results["threats_found"]):
        if threat["id"] == threat_id:
            # In a real app, you would perform different actions based on threat_type
            # For this simulation, we'll just remove it from the list
            _last_scan_results["threats_found"].pop(i)
            return True
            
    return False

def check_app_permissions():
    """
    Check app permissions for possible security issues.
    
    In a real app, this would analyze installed apps' permissions.
    For this simulation, we just return representative data.
    
    Returns:
        list: Apps with potentially dangerous permissions.
    """
    dangerous_permissions = [
        "android.permission.READ_CONTACTS",
        "android.permission.CAMERA",
        "android.permission.ACCESS_FINE_LOCATION",
        "android.permission.RECORD_AUDIO",
        "android.permission.READ_SMS",
        "android.permission.SEND_SMS"
    ]
    
    suspicious_apps = [
        {
            "app_name": "Free Flashlight",
            "package": "com.suspicious.flashlight",
            "permissions": ["android.permission.ACCESS_FINE_LOCATION", "android.permission.CAMERA", "android.permission.READ_CONTACTS"],
            "risk_level": "high"
        },
        {
            "app_name": "Quick Calculator",
            "package": "com.calculator.quick",
            "permissions": ["android.permission.READ_CONTACTS", "android.permission.SEND_SMS"],
            "risk_level": "medium"
        }
    ]
    
    return suspicious_apps

def start_realtime_scanner():
    """
    Mulai pemindai keamanan real-time yang berjalan di latar belakang.
    
    Di aplikasi nyata, ini akan mengatur proses layanan Android.
    Untuk simulasi ini, kita hanya mengatur status.
    
    Returns:
        bool: True jika pemindai berhasil dimulai.
    """
    global _realtime_scan_active
    _realtime_scan_active = True
    
    # Tambahkan log aktivitas
    add_activity_log("Scanner Real-Time", "Pemindaian real-time dimulai dan aktif melindungi perangkat Anda.")
    
    return True

def stop_realtime_scanner():
    """
    Hentikan pemindai keamanan real-time.
    
    Returns:
        bool: True jika pemindai berhasil dihentikan.
    """
    global _realtime_scan_active
    _realtime_scan_active = False
    
    # Tambahkan log aktivitas
    add_activity_log("Scanner Real-Time", "Pemindaian real-time dihentikan. Perangkat Anda tidak dilindungi.")
    
    return True

def is_realtime_scanner_active():
    """
    Periksa apakah pemindai real-time sedang aktif.
    
    Returns:
        bool: Status pemindai real-time.
    """
    global _realtime_scan_active
    return _realtime_scan_active

def scan_with_ai():
    """
    Lakukan pemindaian mendalam menggunakan algoritma AI.
    
    Di aplikasi nyata, ini akan menggunakan model AI untuk analisis lanjutan.
    Untuk simulasi, kita mengembalikan hasil yang dihasilkan.
    
    Returns:
        dict: Hasil pemindaian AI dengan deteksi pola dan ancaman canggih.
    """
    time.sleep(3)  # Simulasi analisis AI yang lebih lama
    
    ai_results = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ai_model_version": "3.2.1",
        "advanced_threats": [
            {
                "id": "ai-threat-001",
                "type": "hidden_malware",
                "name": "Trojan.Android.BankStealer",
                "description": "Malware tersembunyi yang mendeteksi aplikasi perbankan dan mencoba mencuri kredensial.",
                "detection_confidence": 94.7,
                "risk_level": "critical"
            },
            {
                "id": "ai-threat-002",
                "type": "behavior_pattern",
                "name": "Suspicious Background Activity",
                "description": "Pola aktivitas mencurigakan terdeteksi dari aplikasi yang diam-diam mengakses data kontak.",
                "detection_confidence": 87.2,
                "risk_level": "high"
            }
        ],
        "suspicious_behaviors": [
            {
                "app_name": "Photo Editor Pro",
                "behavior": "Akses kamera saat aplikasi tidak digunakan",
                "frequency": "8 kali dalam 24 jam terakhir"
            },
            {
                "app_name": "Weather Plus",
                "behavior": "Transmisi data yang tidak terenkripsi ke server yang tidak dikenal",
                "frequency": "Terus-menerus saat terhubung ke WiFi"
            }
        ]
    }
    
    # Tambahkan ke log aktivitas
    add_activity_log("Pemindaian AI", "Analisis AI mendalam selesai, menemukan pola dan ancaman tingkat lanjut.")
    
    return ai_results

def firewall_block_connection(app_name, destination, port):
    """
    Blokir koneksi jaringan dari aplikasi tertentu.
    
    Di aplikasi nyata, ini akan menyiapkan aturan firewall.
    Untuk simulasi, kita hanya menyimpan tindakan.
    
    Args:
        app_name (str): Nama aplikasi yang diblokir.
        destination (str): Alamat tujuan.
        port (int): Port tujuan.
        
    Returns:
        bool: True jika pemblokiran berhasil.
    """
    global _firewall_blocks
    
    block = {
        "id": f"block-{len(_firewall_blocks) + 1}",
        "app": app_name,
        "destination": destination,
        "port": port,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    _firewall_blocks.append(block)
    
    # Tambahkan log aktivitas
    add_activity_log("Firewall Pintar", f"Koneksi dari {app_name} ke {destination}:{port} diblokir.")
    
    return True

def get_firewall_blocks():
    """
    Dapatkan daftar koneksi yang diblokir oleh firewall.
    
    Returns:
        list: Daftar koneksi yang diblokir.
    """
    global _firewall_blocks
    return _firewall_blocks

def add_activity_log(source, message):
    """
    Tambahkan entri ke log aktivitas keamanan.
    
    Args:
        source (str): Sumber log (pemindai, firewall, dll).
        message (str): Pesan log.
        
    Returns:
        dict: Entri log yang dibuat.
    """
    global _activity_logs
    
    log_entry = {
        "id": f"log-{len(_activity_logs) + 1}",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "source": source,
        "message": message
    }
    
    _activity_logs.append(log_entry)
    
    # Batasi log ke 100 entri terakhir
    if len(_activity_logs) > 100:
        _activity_logs = _activity_logs[-100:]
        
    return log_entry

def get_activity_logs():
    """
    Dapatkan log aktivitas keamanan.
    
    Returns:
        list: Daftar log aktivitas.
    """
    global _activity_logs
    return _activity_logs

def check_privacy_violations():
    """
    Periksa aplikasi yang melanggar privasi pengguna.
    
    Returns:
        list: Daftar pelanggaran privasi.
    """
    violations = [
        {
            "app_name": "Social Media App",
            "package": "com.socialmedia.app",
            "violations": [
                {
                    "type": "camera_access",
                    "description": "Mengakses kamera tanpa pemberitahuan",
                    "frequency": "5 kali dalam seminggu terakhir"
                },
                {
                    "type": "location_tracking",
                    "description": "Melacak lokasi saat aplikasi tidak digunakan",
                    "frequency": "Terus-menerus"
                }
            ],
            "risk_level": "high"
        },
        {
            "app_name": "News Reader",
            "package": "com.news.reader",
            "violations": [
                {
                    "type": "contacts_access",
                    "description": "Membaca kontak tanpa perlu",
                    "frequency": "Setiap kali aplikasi dimulai"
                }
            ],
            "risk_level": "medium"
        }
    ]
    
    return violations

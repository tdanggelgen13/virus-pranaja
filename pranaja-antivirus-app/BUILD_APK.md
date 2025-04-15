# Panduan Mem-build APK untuk Pranaja Anti-Virus

## Prasyarat
1. Instal Node.js dan npm
2. Instal Android Studio dan Android SDK
3. Konfigurasi SDK, environment variables (ANDROID_SDK_ROOT, JAVA_HOME)
4. Instal Gradle build tool

## Langkah-langkah Build APK

### 1. Clone repositori dan atur dependensi
```bash
# Clone repositori (jika menggunakan Git)
git clone <URL_REPOSITORI>
cd pranaja-antivirus

# Atau ekstrak paket yang diunduh
# ...

# Instal dependensi
npm install
```

### 2. Siapkan Capacitor
```bash
# Jika belum ada yang terinstal
npm install @capacitor/core @capacitor/cli @capacitor/android

# Sync aplikasi dengan platform android
npx cap sync android
```

### 3. Build APK menggunakan Android Studio
```bash
# Buka project di Android Studio
npx cap open android

# Atau buka manual folder android di Android Studio
```

Di Android Studio:
1. Pilih menu `Build` -> `Build Bundle(s) / APK(s)` -> `Build APK(s)`
2. Tunggu proses build selesai
3. APK akan tersedia di `android/app/build/outputs/apk/debug/app-debug.apk`

### 4. Build APK menggunakan Command Line (alternatif)
```bash
cd android
./gradlew assembleDebug
```

APK akan tersedia di `android/app/build/outputs/apk/debug/app-debug.apk`

## Instalasi di Perangkat Android

1. Transfer APK ke perangkat Android via USB, Bluetooth, atau upload ke cloud
2. Buka file manager di Android dan buka file APK
3. Jika diminta, aktifkan "Install dari sumber tidak dikenal" di pengaturan keamanan
4. Ikuti panduan instalasi di layar

## Catatan untuk Produksi

Untuk release produksi, lakukan langkah tambahan:
1. Buat keystore untuk signing APK
2. Konfigurasikan build.gradle dengan keystore
3. Build APK release dengan perintah `./gradlew assembleRelease`

APK release akan tersedia di `android/app/build/outputs/apk/release/app-release.apk`

## Troubleshooting

1. Jika mengalami error saat build, periksa log build di Android Studio
2. Pastikan SDK Tools up-to-date
3. Periksa konfigurasi Gradle version di project
4. Jika perubahan tidak terlihat, jalankan `npx cap sync` sebelum build ulang
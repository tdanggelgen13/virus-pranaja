def get_topics():
    """
    Get a list of educational topics about mobile security.
    
    Returns:
        list: Topics with title, summary, and ID.
    """
    return [
        {
            "id": "mobile-malware",
            "title": "Mobile Malware: Types and Prevention",
            "summary": "Learn about different types of mobile malware and how to prevent infections.",
            "icon": "shield-exclamation"
        },
        {
            "id": "phishing",
            "title": "Phishing Attacks on Mobile",
            "summary": "Understand how phishing attacks target mobile users and ways to stay safe.",
            "icon": "fish"
        },
        {
            "id": "app-permissions",
            "title": "Understanding App Permissions",
            "summary": "Why app permissions matter and how to manage them for better privacy.",
            "icon": "lock"
        },
        {
            "id": "secure-wifi",
            "title": "Secure Wi-Fi Practices",
            "summary": "Best practices for using public Wi-Fi and securing your home network.",
            "icon": "wifi"
        },
        {
            "id": "password-security",
            "title": "Password and Authentication Security",
            "summary": "Create strong passwords and understand different authentication methods.",
            "icon": "key"
        },
        {
            "id": "data-encryption",
            "title": "Data Encryption on Android",
            "summary": "How encryption protects your data and how to ensure your device is encrypted.",
            "icon": "lock-keyhole"
        }
    ]

def get_topic_content(topic_id):
    """
    Get detailed content for a specific educational topic.
    
    Args:
        topic_id (str): The ID of the topic to retrieve.
        
    Returns:
        dict: The topic content or None if not found.
    """
    topics_content = {
        "mobile-malware": {
            "title": "Mobile Malware: Types and Prevention",
            "sections": [
                {
                    "heading": "What is Mobile Malware?",
                    "content": """
                    Mobile malware refers to malicious software specifically designed to target mobile devices like smartphones and tablets. Unlike traditional computer malware, mobile malware exploits the unique features and vulnerabilities of mobile operating systems and the way people use their mobile devices.
                    
                    Mobile devices are particularly attractive targets for attackers because they often contain personal information, banking details, and are constantly connected to the internet.
                    """
                },
                {
                    "heading": "Common Types of Mobile Malware",
                    "content": """
                    1. **Adware**: Displays unwanted advertisements, often in an aggressive or deceptive manner.
                    
                    2. **Spyware**: Monitors user activities without their knowledge, collecting personal information, location data, or communications.
                    
                    3. **Trojans**: Disguised as legitimate apps but perform malicious actions in the background.
                    
                    4. **Ransomware**: Locks a device or encrypts its data, demanding payment for restoration.
                    
                    5. **Banking Trojans**: Specifically target banking credentials and financial information.
                    
                    6. **SMS Malware**: Sends premium-rate messages from infected devices, resulting in charges to the user.
                    """
                },
                {
                    "heading": "How Devices Get Infected",
                    "content": """
                    - **Unofficial App Stores**: Downloading apps from sources other than the Google Play Store.
                    
                    - **Malicious Apps**: Even legitimate app stores can occasionally host malicious apps.
                    
                    - **Phishing**: Clicking on malicious links in emails, messages, or websites.
                    
                    - **Drive-by Downloads**: Malware that downloads automatically when visiting infected websites.
                    
                    - **Direct-to-Device Attacks**: Exploiting vulnerabilities in Bluetooth, WiFi, or other connections.
                    """
                },
                {
                    "heading": "Warning Signs of Infection",
                    "content": """
                    - Unexpected battery drain
                    - Unusual data usage
                    - Device overheating
                    - Performance slowdowns
                    - Pop-up advertisements
                    - Unfamiliar apps appearing
                    - Unexpected charges on your bill
                    """
                },
                {
                    "heading": "Prevention Best Practices",
                    "content": """
                    1. **Only download apps from official sources** like the Google Play Store.
                    
                    2. **Check app permissions** before installing and question why apps need certain access.
                    
                    3. **Keep your device updated** with the latest security patches and OS updates.
                    
                    4. **Install a reputable security app** that can scan for malware.
                    
                    5. **Be cautious of links** in emails, text messages, and social media.
                    
                    6. **Disable "Install from Unknown Sources"** in your security settings.
                    
                    7. **Regularly review installed apps** and remove those you no longer use.
                    
                    8. **Be skeptical of "too good to be true"** offers, giveaways, or prizes.
                    """
                }
            ]
        },
        "phishing": {
            "title": "Phishing Attacks on Mobile",
            "sections": [
                {
                    "heading": "Understanding Mobile Phishing",
                    "content": """
                    Phishing on mobile devices involves attempts to trick users into revealing sensitive information like passwords, credit card numbers, or personal data through deceptive communications. Mobile phishing can be particularly effective because:
                    
                    - Smaller screens make it harder to spot suspicious elements
                    - Mobile interfaces often hide full URLs and security indicators
                    - People tend to be more distracted when using mobile devices
                    - Mobile users often check messages immediately upon receipt
                    """
                },
                {
                    "heading": "Common Mobile Phishing Techniques",
                    "content": """
                    1. **SMS Phishing (Smishing)**: Sending text messages that appear to be from trusted sources with malicious links.
                    
                    2. **Email Phishing**: Traditional email phishing adapted for mobile interfaces.
                    
                    3. **In-App Phishing**: Malicious ads or pop-ups within legitimate apps.
                    
                    4. **Voice Phishing (Vishing)**: Phone calls that attempt to trick users into revealing sensitive information.
                    
                    5. **QR Code Phishing**: Malicious QR codes that direct to phishing websites.
                    
                    6. **Social Media Phishing**: Deceptive messages, posts, or ads on social platforms.
                    """
                },
                {
                    "heading": "Real-World Examples",
                    "content": """
                    - Text messages claiming to be from delivery services requesting "updated delivery information"
                    
                    - Banking alerts about "suspicious activity" requiring immediate verification
                    
                    - "Account locked" notifications from email or social media providers
                    
                    - COVID-19 related scams offering vaccine information or financial assistance
                    
                    - Fake login pages for popular services (Netflix, Google, Facebook, etc.)
                    """
                },
                {
                    "heading": "How to Protect Yourself",
                    "content": """
                    1. **Verify the sender** by contacting the company directly through official channels.
                    
                    2. **Don't click on suspicious links** in texts, emails, or social media messages.
                    
                    3. **Check for spelling and grammar errors** which are common in phishing attempts.
                    
                    4. **Be wary of urgent requests** that pressure you to act immediately.
                    
                    5. **Manually type URLs** instead of clicking links when dealing with sensitive information.
                    
                    6. **Use multi-factor authentication** wherever possible.
                    
                    7. **Install security apps** that can detect and block phishing attempts.
                    
                    8. **Report phishing attempts** to the spoofed organization and relevant authorities.
                    """
                },
                {
                    "heading": "What to Do If You've Been Phished",
                    "content": """
                    1. **Change your passwords immediately** for any compromised accounts.
                    
                    2. **Contact your bank or credit card company** if financial information was compromised.
                    
                    3. **Monitor your accounts** for suspicious activity.
                    
                    4. **Report the incident** to relevant organizations and authorities.
                    
                    5. **Consider identity theft protection services** for serious breaches.
                    """
                }
            ]
        },
        "app-permissions": {
            "title": "Understanding App Permissions",
            "sections": [
                {
                    "heading": "Why App Permissions Matter",
                    "content": """
                    App permissions control what information and device features an app can access. Understanding and managing these permissions is crucial for protecting your privacy and security. When you grant permissions, you're allowing apps to:
                    
                    - Access your personal data (contacts, messages, photos)
                    - Use device hardware (camera, microphone, GPS)
                    - Perform actions (send notifications, make calls, use internet)
                    
                    Overly permissive apps can potentially:
                    - Collect excessive data about you
                    - Share your information with third parties
                    - Track your location and activities
                    - Access sensitive information
                    """
                },
                {
                    "heading": "Common Android Permissions Explained",
                    "content": """
                    **High-Sensitivity Permissions:**
                    
                    - **Camera**: Allows the app to take pictures and record videos
                    - **Microphone**: Enables the app to record audio
                    - **Location**: Lets the app know your precise or approximate location
                    - **Contacts**: Gives access to your contact list
                    - **Phone**: Allows making calls, accessing phone state, or call history
                    - **SMS**: Enables reading, sending, or receiving text messages
                    - **Storage**: Provides access to photos, media, and files on your device
                    
                    **Medium-Sensitivity Permissions:**
                    
                    - **Calendar**: Accesses your calendar events
                    - **Activity Recognition**: Detects physical activities (walking, driving)
                    - **Bluetooth**: Connects to Bluetooth devices
                    
                    **Lower-Sensitivity Permissions:**
                    
                    - **Internet**: Allows the app to access the internet
                    - **Notifications**: Enables the app to send you notifications
                    - **Vibration**: Allows the app to control the vibration motor
                    """
                },
                {
                    "heading": "Permission Red Flags",
                    "content": """
                    Be wary when apps request permissions that don't align with their functionality:
                    
                    - A simple game requesting access to your contacts, location, or camera
                    - A flashlight app asking for phone or SMS permissions
                    - A calculator requesting location access or storage permissions
                    - Any app requesting accessibility services without a clear need
                    
                    These mismatched permission requests often indicate that an app may be collecting data for advertising or other purposes unrelated to its core functionality.
                    """
                },
                {
                    "heading": "How to Manage App Permissions",
                    "content": """
                    **On Modern Android Devices (Android 10+):**
                    
                    1. Go to **Settings > Apps & notifications**
                    2. Select an app or tap **See all apps**
                    3. Tap **Permissions**
                    4. Toggle permissions on or off as needed
                    
                    **Alternative Method:**
                    
                    1. Go to **Settings > Privacy > Permission manager**
                    2. Select a permission category to see which apps have that permission
                    3. Modify app permissions as needed
                    
                    **Best Practices:**
                    
                    - Use **"Only while using the app"** for location permissions when available
                    - Consider using **"Ask every time"** for sensitive permissions
                    - Regularly review and audit app permissions
                    - Uninstall apps you no longer use
                    """
                },
                {
                    "heading": "One-Time Permissions and Auto-Reset",
                    "content": """
                    **One-Time Permissions (Android 11+):**
                    For sensitive permissions like camera, microphone, and location, you can select "Only this time" to grant permission just for that single usage.
                    
                    **Permission Auto-Reset (Android 11+):**
                    If you haven't used an app for several months, Android will automatically reset its sensitive permissions. You'll need to grant them again when you next use the app.
                    
                    These features provide additional control over your privacy by ensuring permissions aren't indefinitely active for apps you rarely use.
                    """
                }
            ]
        },
        "secure-wifi": {
            "title": "Secure Wi-Fi Practices",
            "sections": [
                {
                    "heading": "The Risks of Unsecured Wi-Fi",
                    "content": """
                    Public and unsecured Wi-Fi networks present significant security risks:
                    
                    - **Man-in-the-Middle Attacks**: Attackers can position themselves between you and the connection point to intercept your data
                    
                    - **Packet Sniffing**: Capturing data packets transmitted over the network to gather sensitive information
                    
                    - **Evil Twin Attacks**: Rogue hotspots that mimic legitimate networks to steal information
                    
                    - **Session Hijacking**: Taking over your online sessions after you've logged into services
                    
                    - **Malware Distribution**: Networks can be used to spread malware to connected devices
                    """
                },
                {
                    "heading": "Public Wi-Fi Safety Tips",
                    "content": """
                    When using public Wi-Fi at cafes, airports, hotels, or other locations:
                    
                    1. **Verify network names** before connecting. Ask staff for the exact name to avoid "evil twin" networks.
                    
                    2. **Use a VPN (Virtual Private Network)** to encrypt your traffic. This creates a secure tunnel for your data.
                    
                    3. **Enable "Always use HTTPS"** in your browser settings to ensure encrypted connections to websites.
                    
                    4. **Avoid sensitive activities** like online banking or shopping when on public networks.
                    
                    5. **Disable auto-connect features** to prevent automatically joining unknown networks.
                    
                    6. **Turn off file sharing** and AirDrop when in public.
                    
                    7. **Forget the network** when you're done using it.
                    """
                },
                {
                    "heading": "Securing Your Home Wi-Fi",
                    "content": """
                    Protect your home network with these essential security measures:
                    
                    1. **Use strong encryption** (WPA3 if available, or at minimum WPA2). Never use WEP as it's easily cracked.
                    
                    2. **Create a strong, unique password** for your Wi-Fi network. Use at least 12 characters with a mix of letters, numbers, and symbols.
                    
                    3. **Change the default router login credentials** immediately after setup.
                    
                    4. **Update your router's firmware** regularly to patch security vulnerabilities.
                    
                    5. **Enable the router's firewall** for an additional layer of protection.
                    
                    6. **Set up a guest network** for visitors and IoT devices to keep them separate from your main network.
                    
                    7. **Consider changing your SSID** (network name) to something that doesn't identify you personally.
                    
                    8. **Disable WPS (Wi-Fi Protected Setup)** as it can be vulnerable to attacks.
                    """
                },
                {
                    "heading": "Mobile Hotspot Security",
                    "content": """
                    When using your phone as a hotspot:
                    
                    1. **Use a strong password** that's different from your phone's unlock code.
                    
                    2. **Change the default hotspot name** to something that doesn't identify you or your phone model.
                    
                    3. **Turn off the hotspot** when not in active use.
                    
                    4. **Monitor connected devices** and disconnect any you don't recognize.
                    
                    5. **Set data limits** to prevent excessive usage by others.
                    
                    6. **Be aware of your surroundings** when using a hotspot in public places.
                    """
                },
                {
                    "heading": "Signs Your Wi-Fi Might Be Compromised",
                    "content": """
                    Watch for these indicators that someone might be using your Wi-Fi without permission:
                    
                    - Unexplained slow internet speeds
                    - Unfamiliar devices connected to your network
                    - Changed router settings you didn't modify
                    - Increased data usage on your internet bill
                    - Router lights showing activity when you're not using the internet
                    - Unusual outgoing traffic from your network
                    
                    If you suspect unauthorized access, change your Wi-Fi password immediately and consider resetting your router to factory settings.
                    """
                }
            ]
        },
        "password-security": {
            "title": "Password and Authentication Security",
            "sections": [
                {
                    "heading": "Why Password Security Matters",
                    "content": """
                    Strong passwords are your first line of defense against unauthorized access to your accounts and personal information. Password breaches can lead to:
                    
                    - Identity theft
                    - Financial fraud
                    - Email or social media account hijacking
                    - Data theft
                    - Access to your other accounts (through password reuse)
                    
                    The average person has dozens of online accounts, making password management both crucial and challenging.
                    """
                },
                {
                    "heading": "Creating Strong Passwords",
                    "content": """
                    Effective passwords should be:
                    
                    1. **Long** - At least 12 characters, preferably longer
                    
                    2. **Complex** - Include a mix of:
                       - Uppercase letters (A-Z)
                       - Lowercase letters (a-z)
                       - Numbers (0-9)
                       - Special characters (!@#$%^&*)
                    
                    3. **Unique** - Different for each account or service
                    
                    4. **Not personal** - Avoid easily guessable information like:
                       - Birth dates
                       - Names of family members or pets
                       - Addresses
                       - Common words or phrases
                    
                    5. **Unpredictable** - Don't use obvious patterns or substitutions
                    
                    **Password Creation Method:** Consider using the "passphrase" approach - a string of random words with numbers and symbols added, like "correct-horse-battery-staple-42!" which is both strong and memorable.
                    """
                },
                {
                    "heading": "Password Management Best Practices",
                    "content": """
                    Manage your many passwords effectively:
                    
                    1. **Use a password manager** to securely store and generate complex passwords. Popular options include:
                       - Bitwarden (open source)
                       - LastPass
                       - 1Password
                       - Dashlane
                    
                    2. **Enable two-factor authentication (2FA)** wherever available
                    
                    3. **Regularly update critical passwords** every 3-6 months
                    
                    4. **Don't share passwords** across multiple accounts
                    
                    5. **Check for password breaches** using services like HaveIBeenPwned.com
                    
                    6. **Never share passwords** via email, text, or chat
                    
                    7. **Log out** from shared or public devices
                    
                    8. **Be cautious of "remember me"** options on shared devices
                    """
                },
                {
                    "heading": "Beyond Passwords: Authentication Methods",
                    "content": """
                    Modern authentication extends beyond traditional passwords:
                    
                    1. **Two-Factor Authentication (2FA)**
                       - Something you know (password)
                       - Something you have (phone or security key)
                       - Something you are (biometric)
                    
                    2. **Biometric Authentication**
                       - Fingerprint readers
                       - Facial recognition
                       - Voice recognition
                       - Iris scanners
                    
                    3. **Hardware Security Keys**
                       - Physical USB, NFC, or Bluetooth devices
                       - Often using the FIDO U2F standard
                    
                    4. **Authenticator Apps**
                       - Google Authenticator
                       - Authy
                       - Microsoft Authenticator
                       - Generates time-based one-time passwords (TOTP)
                    
                    5. **Single Sign-On (SSO)**
                       - Using one account to access multiple services
                       - "Sign in with Google/Apple/Facebook"
                    """
                },
                {
                    "heading": "Mobile-Specific Authentication Tips",
                    "content": """
                    For your Android device:
                    
                    1. **Use a strong screen lock** (PIN, pattern, password, or biometric)
                    
                    2. **Set up fingerprint or facial recognition** as convenient but secure options
                    
                    3. **Use a PIN with at least 6 digits** rather than the minimum 4
                    
                    4. **Avoid pattern locks** that can be observed over your shoulder
                    
                    5. **Enable "Find My Device"** to locate or erase your phone remotely if lost
                    
                    6. **Consider app locks** for sensitive applications like banking or messaging
                    
                    7. **Review apps with access to Accessibility Services** and ensure they're trusted
                    
                    8. **Be cautious of "smart unlock"** features that bypass your lock screen
                    """
                }
            ]
        },
        "data-encryption": {
            "title": "Data Encryption on Android",
            "sections": [
                {
                    "heading": "Understanding Encryption",
                    "content": """
                    Encryption is the process of converting information into a code to prevent unauthorized access. On mobile devices, encryption protects:
                    
                    - Personal photos and videos
                    - Messages and emails
                    - Contacts and calendar data
                    - Saved passwords and account information
                    - Health and financial data
                    - Documents and notes
                    
                    Without encryption, if your device is lost, stolen, or compromised, someone could potentially access all your data, even if they bypass your lock screen.
                    """
                },
                {
                    "heading": "How Android Encryption Works",
                    "content": """
                    Modern Android devices use **full-disk encryption** or **file-based encryption**:
                    
                    **Full-Disk Encryption (FDE):**
                    - Encrypts the entire device storage as a single unit
                    - All data is protected with a single key derived from your device password
                    - Used on older Android devices (pre-Android 7.0)
                    - Requires password entry before boot completes
                    
                    **File-Based Encryption (FBE):**
                    - Encrypts different files with different keys
                    - Allows the device to boot to the lock screen before decryption
                    - Enables some functionality (like alarms) before unlock
                    - Can have different security levels for different files
                    - Standard on Android 7.0 and newer devices
                    
                    Both methods protect your data if your device falls into the wrong hands.
                    """
                },
                {
                    "heading": "Checking and Enabling Encryption",
                    "content": """
                    **Check Encryption Status:**
                    
                    1. Go to **Settings > Security** (or Security & location)
                    2. Look for "Encryption" or "Encryption & credentials"
                    3. It should indicate if your device is encrypted
                    
                    **Enable Encryption (if not already enabled):**
                    
                    1. Ensure your battery is at least 80% charged and the device is plugged in
                    2. Go to **Settings > Security > Encryption**
                    3. Select **"Encrypt phone"** or similar option
                    4. Follow the prompts to complete the process
                    
                    Note: Most modern Android devices (Android 6.0+) are encrypted by default, but it's good to verify.
                    """
                },
                {
                    "heading": "Beyond Device Encryption",
                    "content": """
                    Additional encryption options to protect specific data:
                    
                    1. **Secure Folder** (on Samsung devices)
                       - Creates an encrypted space for sensitive apps and files
                       - Protected by a separate password or biometric
                    
                    2. **Encrypted messaging apps**
                       - Signal
                       - WhatsApp
                       - Telegram (Secret Chats)
                       - Use end-to-end encryption for communications
                    
                    3. **Password managers**
                       - Store sensitive information in encrypted vaults
                    
                    4. **File encryption apps**
                       - Encrypt specific files and folders
                       - Often use AES-256 encryption
                    
                    5. **Encrypted notes applications**
                       - Protect specific notes with additional encryption
                    """
                },
                {
                    "heading": "The Role of Your Lock Screen",
                    "content": """
                    Your lock screen is directly tied to encryption security:
                    
                    - The strength of your PIN, password, or pattern affects encryption security
                    - A 4-digit PIN offers much less protection than a longer password
                    - Biometric methods (fingerprint, face) are convenient but can be less secure in some situations
                    
                    **Recommendations:**
                    
                    1. Use a strong PIN (6+ digits) or password rather than a pattern
                    2. Enable biometrics for convenience, but be aware they can be bypassed in some situations
                    3. Set automatic lock timing to be reasonably short (30 seconds to 1 minute)
                    4. Disable lock screen notifications for sensitive apps
                    """
                },
                {
                    "heading": "Encryption Limitations",
                    "content": """
                    Understanding what encryption doesn't protect against:
                    
                    1. **Malware and spyware:** Encryption doesn't prevent malicious apps from accessing your data when the device is unlocked and being used.
                    
                    2. **Unlocked devices:** Data is vulnerable when your device is unlocked.
                    
                    3. **Cloud storage:** Data backed up to the cloud follows the security practices of the cloud provider.
                    
                    4. **Legal access:** In some jurisdictions, authorities may legally compel you to unlock your device.
                    
                    5. **Weak passwords:** Encryption is only as strong as the password protecting it.
                    
                    6. **Social engineering:** Someone tricking you into providing access circumvents encryption.
                    """
                }
            ]
        }
    }
    
    return topics_content.get(topic_id)

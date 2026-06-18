import datetime

# --- Araç Tanımlamaları (Tool Definitions) ---
# Bu fonksiyonlar, ajanların kullanabileceği harici araçları veya servisleri temsil eder.
# These functions represent external tools or services that agents can utilize.

def get_current_time():
    """Mevcut zamanı döndüren bir araç."""
    # Gerçek bir senaryoda, bu bir sistem çağrısı veya harici bir API isteği olabilir.
    return datetime.datetime.now().strftime("%H:%M:%S")

def fetch_weather_data(location="Ankara"):
    """Belirtilen konum için hava durumu bilgisini döndüren bir araç."""
    # Gerçek bir senaryoda, bu bir hava durumu API'sine yapılan bir HTTP isteği olabilir.
    return f"Hava durumu: {location} için parçalı bulutlu, 15°C."

# --- Araç Kayıt Defteri (Tool Registry) ---
# Bu sözlük, mevcut araçları ve onlara erişim yöntemlerini tutar.
# Ajanlar, ihtiyaç duydukları araçları buradan keşfeder.
# This dictionary holds available tools and their access methods.
# Agents discover the tools they need from here.

tool_registry = {
    "get_time": get_current_time,
    "get_weather": fetch_weather_data
}

# --- Ajan Tanımlaması (Agent Definition) ---
# Bu ajan, belirli bir görevi tamamlamak için araçları keşfeder ve kullanır.
# This agent discovers and uses tools to complete a specific task.

def orchestrate_task(task_description, registry):
    print(f"\n[Ajan]: '{task_description}' görevini üstleniyor.")

    # Ajanın görevi analiz etmesi ve gerekli araçları belirlemesi
    # Agent analyzes the task and identifies necessary tools
    if "zamanı öğren" in task_description.lower():
        # --- Araç Keşfi ve Etkileşim (Tool Discovery and Interaction) ---
        # Ajan, 'get_time' aracını kayıt defterinde arar.
        # Agent looks for the 'get_time' tool in the registry.
        if "get_time" in registry:
            print("[Ajan]: 'get_time' aracını keşfetti ve kullanıyor...")
            current_time = registry["get_time"]() # Keşfedilen aracı çağırır / Invokes the discovered tool
            print(f"[Ajan]: Şu anki zaman: {current_time}")
        else:
            print("[Ajan]: 'get_time' aracı bulunamadı. Görev tamamlanamadı.")

    if "hava durumunu öğren" in task_description.lower():
        # --- Araç Keşfi ve Etkileşim (Tool Discovery and Interaction) ---
        # Ajan, 'get_weather' aracını kayıt defterinde arar.
        # Agent looks for the 'get_weather' tool in the registry.
        if "get_weather" in registry:
            print("[Ajan]: 'get_weather' aracını keşfetti ve kullanıyor...")
            # Araca parametre ileterek etkileşim kurar / Interacts with the tool by passing a parameter
            weather_info = registry["get_weather"]("Istanbul") 
            print(f"[Ajan]: Hava durumu bilgisi: {weather_info}")
        else:
            print("[Ajan]: 'get_weather' aracı bulunamadı. Görev tamamlanamadı.")

    print(f"[Ajan]: '{task_description}' görevi tamamlandı.")

# --- Ana Çalışma (Main Execution) ---
if __name__ == "__main__":
    print("--- Ajan ve Araç Etkileşimi Simülasyonu Başladı ---")

    # Ajanın birden fazla araç gerektiren bir görevi yerine getirmesi
    orchestrate_task("Güncel zamanı ve İstanbul hava durumunu öğren.", tool_registry)

    # Ajanın sadece tek bir araç gerektiren bir görevi yerine getirmesi
    orchestrate_task("Sadece zamanı öğren.", tool_registry)

    # Bir aracın eksik olduğu senaryo (simülasyon için geçici olarak kaldırılabilir)
    # del tool_registry["get_weather"]
    # orchestrate_task("Hava durumunu öğren.", tool_registry)

    print("--- Simülasyon Sona Erdi ---")

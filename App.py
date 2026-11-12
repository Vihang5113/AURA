import streamlit as st
import random

# -------------------------------------------------------------
# 1. SETUP & SIMULATED SPACE SENSORS (GATHER)
# -------------------------------------------------------------
st.set_page_config(page_title="AURA - Space Health", page_icon="🚀", layout="wide")

st.title("🚀 AURA: Crew Autonomous Health Center")
st.caption("Operating 100% Offline | Mars Mission Simulation Mode")
st.markdown("---")

# Simulate live telemetry data from astronaut suit/cabin
simulated_heart_rate = random.randint(65, 115)       # Normal is 60-80, stressed is 100+
simulated_radiation = round(random.uniform(0.1, 5.5), 2) # Normal is < 1.0 mSv/hr
simulated_sleep = random.randint(4, 8)                # Normal is 7-8 hours

# -------------------------------------------------------------
# 2. THE TRAFFIC LIGHT ENGINE (EVALUATE)
# -------------------------------------------------------------
# Determine System Statuses based on thresholds
if simulated_heart_rate > 100:
    cardio_status = "🔴 CRITICAL"
    cardio_color = "red"
elif simulated_heart_rate > 85:
    cardio_status = "🟡 WARNING"
    cardio_color = "orange"
else:
    cardio_status = "🟢 NOMINAL"
    cardio_color = "green"

if simulated_radiation > 4.0:
    rad_status = "🔴 DANGER"
    rad_color = "red"
elif simulated_radiation > 1.5:
    rad_status = "🟡 ELEVATED"
    rad_color = "orange"
else:
    rad_status = "🟢 NOMINAL"
    rad_color = "green"

if simulated_sleep < 5:
    sleep_status = "🟡 FATIGUE RISK"
    sleep_color = "orange"
else:
    sleep_status = "🟢 NOMINAL"
    sleep_color = "green"

# -------------------------------------------------------------
# 3. DISPLAY THE DASHBOARD UI
# -------------------------------------------------------------
st.subheader("📊 Live Telemetry Evaluation")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Heart Rate", value=f"{simulated_heart_rate} BPM")
    st.markdown(f"Status: :{cardio_color}[**{cardio_status}**]")

with col2:
    st.metric(label="Cabin Radiation", value=f"{simulated_radiation} mSv/hr")
    st.markdown(f"Status: :{rad_color}[**{rad_status}**]")

with col3:
    st.metric(label="Crew Sleep (Last 24h)", value=f"{simulated_sleep} Hours")
    st.markdown(f"Status: :{sleep_color}[**{sleep_status}**]")

st.markdown("---")

# -------------------------------------------------------------
# 4. ASTRONAUT CHECK-IN & LOCAL TEXT ANALYSIS (GATHER + EVALUATE)
# -------------------------------------------------------------
st.subheader("🧠 Daily Behavioral Check-in")
user_journal = st.text_area("Type your daily log here (e.g., how you are physically or mentally feeling):", 
                            placeholder="Example: I feel very tired and lonely today...")

behavioral_status = "🟢 NOMINAL"
behavioral_color = "green"

if user_journal:
    # Local keyword check (Simulating offline AI sentiment analysis)
    danger_words = ["lonely", "depressed", "dizzy", "tired", "exhausted", "pain", "hurt"]
    found_words = [word for word in danger_words if word in user_journal.lower()]
    
    if found_words:
        behavioral_status = "🟡 STRESS DETECTED"
        behavioral_color = "orange"
        st.warning(f"Note Analysis: Detected flags indicating fatigue/isolation Indicators: {', '.join(found_words)}")
    else:
        st.success("Note Analysis: Mental state appears stable.")

# -------------------------------------------------------------
# 5. CLOSED-LOOP PROTOCOLS (ACT)
# -------------------------------------------------------------
st.subheader("🏃♂️ Autonomous Action Protocols")
st.write("Based on your current telemetry and logs, execute the following countermeasures immediately:")

# Action triggered by Heart Rate or Text Stress
if cardio_status == "🔴 CRITICAL" or behavioral_status == "🟡 STRESS DETECTED":
    st.error("🚨 **Action Required: Cardiovascular / Mental Stress**")
    if st.button("▶️ Begin 15-Min Guided Breathing & Circadian Light Reset"):
        st.info("Initiating blue-enriched light shifts in Habitat Zone 1 to decrease cortisol levels...")

# Action triggered by Radiation
if rad_status == "🔴 DANGER":
    st.error("☢️ **CRITICAL ALERT: Solar Particle Event**")
    if st.button("🚨 Open Emergency Route to Storm Shelter"):
        st.info("Route mapped: Proceed to the central core module water-wall shield immediately.")
elif rad_status == "🟡 ELEVATED":
    st.warning("⚠️ **Precautionary Action: Radiation Spike**")
    st.write("- Limit extravehicular activity (EVA).\n- Wear personal shielding vests inside the habitat.")

# Action triggered by Sleep
if sleep_status == "🟡 FATIGUE RISK":
    st.warning("💤 **Action Required: Circadian Disruption**")
    if st.button("🔧 Re-schedule Daily Task Load"):
        st.info("Automated Request Sent: Shifting heavy maintenance tasks forward by 12 hours to prioritize crew rest.")

# Default protocol if everything is green
if cardio_status == "🟢 NOMINAL" and rad_status == "🟢 NOMINAL" and sleep_status == "🟢 NOMINAL" and behavioral_status == "🟢 NOMINAL":
    st.success("✅ All health systems nominal. Continue with standard daily mission protocols.")


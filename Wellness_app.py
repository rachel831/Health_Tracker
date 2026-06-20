# ============================================================
#   🌿 Daily Wellness Dashboard — Streamlit Web App
#   Code Your Wellness | CS Girlies Workshop
#   By Rachel Ingabire — INGRA DIGITAL HUB
# ============================================================

import streamlit as st

# ── PAGE CONFIG ─────────────────────────────────────────────
st.set_page_config(
    page_title="Daily Wellness Tracker 🌸",
    page_icon="🌿",
    layout="centered"
)

# ── CUSTOM CSS ───────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

    /* Force light background everywhere */
    html, body, [class*="css"], .stApp {
        background-color: #FFF0F5 !important;
        font-family: 'Poppins', sans-serif !important;
        color: #2D2D2D !important;
    }

    /* Main content area */
    .block-container {
        background-color: #FFF0F5 !important;
        padding-top: 2rem !important;
    }

    /* Input boxes */
    div[data-testid="stNumberInput"] input {
        background-color: #FFFFFF !important;
        color: #2D2D2D !important;
        border: 1.5px solid #F4C0D1 !important;
        border-radius: 10px !important;
        font-family: 'Poppins', sans-serif !important;
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }

    /* Input labels */
    div[data-testid="stNumberInput"] label {
        color: #C2185B !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
    }

    /* +/- buttons on number inputs */
    div[data-testid="stNumberInput"] button {
        background-color: #F8BBD0 !important;
        color: #880E4F !important;
        border: none !important;
        border-radius: 8px !important;
    }

    /* Check My Wellness button */
    div[data-testid="stButton"]:first-of-type > button {
        background: linear-gradient(135deg, #D4537E, #E91E8C) !important;
        color: white !important;
        border: none !important;
        border-radius: 14px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        width: 100% !important;
        font-family: 'Poppins', sans-serif !important;
        box-shadow: 0 4px 15px rgba(212,83,126,0.35) !important;
        transition: all 0.2s !important;
    }
    div[data-testid="stButton"]:first-of-type > button:hover {
        box-shadow: 0 6px 20px rgba(212,83,126,0.5) !important;
        transform: translateY(-1px) !important;
    }

    /* Reset button */
    div[data-testid="stButton"]:last-of-type > button {
        background: #FFFFFF !important;
        color: #D4537E !important;
        border: 2px solid #F4C0D1 !important;
        border-radius: 14px !important;
        padding: 0.6rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        font-family: 'Poppins', sans-serif !important;
    }
    div[data-testid="stButton"]:last-of-type > button:hover {
        background: #FFF0F5 !important;
        border-color: #D4537E !important;
    }

    /* Progress bars */
    div[data-testid="stProgress"] > div > div {
        background: linear-gradient(90deg, #F48FB1, #D4537E) !important;
        border-radius: 99px !important;
    }
    div[data-testid="stProgress"] > div {
        background-color: #FCE4EC !important;
        border-radius: 99px !important;
    }

    /* Divider */
    hr { border-color: #F4C0D1 !important; }

    /* Markdown text */
    p, li, span { color: #2D2D2D !important; }

    /* Hide streamlit branding */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }
</style>
""", unsafe_allow_html=True)


# ── HEALTH LOGIC ─────────────────────────────────────────────
def analyse(water, sleep, steps, mood):
    score = 0
    tips  = []

    if water >= 8:
        score += 25
        tips.append(("💧", "Hydration queen!", "You crushed your water goal today. Your skin is glowing!"))
    else:
        need = 8 - water
        score += int((water / 8) * 25)
        tips.append(("💧", "Drink more water!", f"You need {need:.0f} more glass{'es' if need != 1 else ''} to hit 8 today. Keep a bottle on your desk!"))

    if sleep >= 7:
        score += 25
        tips.append(("🌙", "Sleep goals!", f"{sleep} hours is perfect. Your brain and body are fully recharged."))
    elif sleep >= 5:
        score += int((sleep / 7) * 25)
        tips.append(("🌙", "Almost there!", f"You got {sleep} hrs. Try to hit 7-8 hours for peak energy and focus."))
    else:
        score += int((sleep / 7) * 25)
        tips.append(("🌙", "Rest up, girlie!", f"Only {sleep} hrs of sleep? Prioritise rest tonight — you deserve it."))

    if steps >= 8000:
        score += 25
        tips.append(("🚶", "Active queen!", f"{steps:,} steps! You are moving and grooving today."))
    elif steps >= 5000:
        score += int((steps / 8000) * 25)
        tips.append(("🚶", "Good movement!", f"{steps:,} steps is solid. Try to reach 8,000 for full points!"))
    else:
        score += int((steps / 8000) * 25)
        tips.append(("🚶", "Time to move!", f"Only {steps:,} steps. Even a 10-min walk adds up — let's go!"))

    if mood >= 8:
        score += 25
        tips.append(("😊", "Radiating joy!", f"Mood {mood}/10 — you are absolutely glowing today!"))
    elif mood >= 5:
        score += int((mood / 10) * 25)
        tips.append(("😊", "Decent vibes!", f"Mood {mood}/10. Try journaling or a short walk to lift it higher."))
    else:
        score += int((mood / 10) * 25)
        tips.append(("😊", "Sending love!", f"Mood {mood}/10. Low days happen. Be gentle with yourself today 💕"))

    return score, tips


def get_score_message(score):
    if score >= 95:   return "Perfect wellness day! You are an absolute icon! 👑"
    elif score >= 80: return "Thriving! You are glowing from the inside out! ✨"
    elif score >= 60: return "Looking good! Keep nurturing yourself! 🌱"
    elif score >= 40: return "A decent start — small wins lead to big changes! 💪"
    else:             return "Your body needs some love today — you got this! 💕"


def get_score_color(score):
    if score >= 80:   return "#2D9B6F"
    elif score >= 60: return "#F06292"
    elif score >= 40: return "#EF9F27"
    else:             return "#D4537E"


# ── SESSION STATE for reset ───────────────────────────────────
if "show_results" not in st.session_state:
    st.session_state.show_results = False
if "submitted_data" not in st.session_state:
    st.session_state.submitted_data = None


def do_submit(water, sleep, steps, mood):
    st.session_state.show_results = True
    st.session_state.submitted_data = (water, sleep, steps, mood)


def do_reset():
    st.session_state.show_results = False
    st.session_state.submitted_data = None


# ── HEADER ───────────────────────────────────────────────────
st.markdown("""
<div style="
    background: linear-gradient(135deg, #F8BBD0, #F48FB1, #EC407A);
    padding: 2.2rem 2rem;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 1.5rem;
    box-shadow: 0 6px 24px rgba(212,83,126,0.25);
">
    <h1 style="color: white; font-size: 2rem; font-weight: 700; margin: 0; text-shadow: 0 2px 8px rgba(0,0,0,0.15);">
        🌿 Daily Wellness Check-in
    </h1>
    <p style="color: #FFF8FC; font-size: 1rem; margin-top: 0.5rem; margin-bottom: 0;">
        Enter your numbers and get your glow-up tips ✨
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    "<p style='color:#C2185B; font-size:0.9rem; text-align:center;'>"
    "<b>By Rachel Ingabire</b> · INGRA DIGITAL HUB · CS Girlies Workshop 🌸</p>",
    unsafe_allow_html=True
)
st.markdown("---")

# ── INPUT or RESULTS ─────────────────────────────────────────
if not st.session_state.show_results:

    st.markdown(
        "<h3 style='color:#C2185B;'>📋 How did you do today?</h3>",
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)
    with col1:
        water = st.number_input("💧 Water intake (glasses)", min_value=0.0, max_value=20.0, value=0.0, step=0.5)
        steps = st.number_input("🚶 Steps walked", min_value=0, max_value=50000, value=0, step=100)
    with col2:
        sleep = st.number_input("🌙 Sleep hours", min_value=0.0, max_value=12.0, value=0.0, step=0.5)
        mood  = st.number_input("😊 Mood score (1–10)", min_value=1, max_value=10, value=5, step=1)

    st.markdown("")
    st.button("✨ Check My Wellness", on_click=do_submit, args=(water, sleep, steps, mood))

else:
    # ── RESULTS ──────────────────────────────────────────────
    water, sleep, steps, mood = st.session_state.submitted_data
    score, tips = analyse(water, sleep, steps, mood)
    color = get_score_color(score)

    # Score card
    st.markdown(f"""
    <div style="
        background: white;
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 4px 20px rgba(212,83,126,0.12);
        border: 1.5px solid #F4C0D1;
        margin-bottom: 1.25rem;
    ">
        <p style="color: #888; font-size: 0.9rem; margin-bottom: 0.25rem;">Your wellness score today</p>
        <h1 style="color: {color}; font-size: 4rem; font-weight: 800; margin: 0;">{score}%</h1>
        <p style="color: #555; font-style: italic; font-size: 1rem; margin-top: 0.25rem;">
            {get_score_message(score)}
        </p>
    </div>
    """, unsafe_allow_html=True)

    # Metrics
    st.markdown("<h4 style='color:#C2185B;'>📊 How you did today</h4>", unsafe_allow_html=True)

    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown(f"""
        <div style="background:white; border-radius:14px; padding:1rem; text-align:center;
                    box-shadow:0 2px 10px rgba(212,83,126,0.1); border:1px solid #F4C0D1;">
            <div style="font-size:1.5rem">💧</div>
            <div style="color:#888; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em;">Water</div>
            <div style="color:#C2185B; font-weight:700; font-size:1.05rem;">{water:.0f} / 8 glasses</div>
        </div>""", unsafe_allow_html=True)
        st.progress(min(water / 8, 1.0))

    with m2:
        st.markdown(f"""
        <div style="background:white; border-radius:14px; padding:1rem; text-align:center;
                    box-shadow:0 2px 10px rgba(212,83,126,0.1); border:1px solid #F4C0D1;">
            <div style="font-size:1.5rem">🌙</div>
            <div style="color:#888; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em;">Sleep</div>
            <div style="color:#C2185B; font-weight:700; font-size:1.05rem;">{sleep} / 8 hrs</div>
        </div>""", unsafe_allow_html=True)
        st.progress(min(sleep / 8, 1.0))

    with m3:
        st.markdown(f"""
        <div style="background:white; border-radius:14px; padding:1rem; text-align:center;
                    box-shadow:0 2px 10px rgba(212,83,126,0.1); border:1px solid #F4C0D1;">
            <div style="font-size:1.5rem">🚶</div>
            <div style="color:#888; font-size:0.75rem; text-transform:uppercase; letter-spacing:0.05em;">Steps</div>
            <div style="color:#C2185B; font-weight:700; font-size:1.05rem;">{steps:,}</div>
        </div>""", unsafe_allow_html=True)
        st.progress(min(steps / 8000, 1.0))

    # Tips
    st.markdown("<h4 style='color:#C2185B; margin-top:1.25rem;'>💕 Your personal wellness tips</h4>", unsafe_allow_html=True)

    for emoji, title, body in tips:
        st.markdown(f"""
        <div style="
            background: white;
            border-radius: 14px;
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            box-shadow: 0 2px 10px rgba(212,83,126,0.08);
            border-left: 5px solid #F48FB1;
        ">
            <div style="font-weight: 700; color: #880E4F; font-size: 1rem; margin-bottom: 0.2rem;">
                {emoji} {title}
            </div>
            <div style="color: #555; font-size: 0.92rem;">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Reset button
    st.button("↩ Start Over", on_click=do_reset)

    st.markdown(
        "<p style='color:#BBBBBB; font-size:0.8rem; text-align:center; margin-top:1rem;'>"
        "🌿 Built with Python & Streamlit · By Rachel Ingabire · racheltechguide.blogspot.com</p>",
        unsafe_allow_html=True
    )


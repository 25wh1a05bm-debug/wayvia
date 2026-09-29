# WAYVIA — “Find Your Way. Your Way.”

> **AI-Powered Accessibility Intelligence & Personalized Location Discovery Platform**  
> *Built by Team Vertex • Designed from the WAYVIA Presentation Design System*

---

## 🌟 Overview & Product Philosophy

Traditional location search platforms answer:
> **“Where is this place?”**

**WAYVIA** solves the much more critical, personal question:
> **“Is this place suitable for ME?”**

WAYVIA combines **Google Maps Platform**, **Places API (New)**, and **Gemini Multimodal Intelligence** to transform scattered venue details, photos, and reviews into a structured, three-state decision-making experience:
$$\text{SEARCH} \longrightarrow \text{UNDERSTAND} \longrightarrow \text{MATCH} \longrightarrow \text{DECIDE}$$

---

## 🎨 Visual Identity & Presentation Theme

The application directly transforms the uploaded **WAYVIA Team Vertex Presentation** into a living, responsive web product:
- **Presentation Wallpaper**: Pastel sky-blue (`#98D7F7`) and ivory/cream (`#FFFDF8`) vertical striped backdrop.
- **Brand Typography**:
  - Signature Cursive Script: `Playball` & `Satisfy` for the iconic *"Way Via"* title with crisp white sticker offset drop shadows.
  - High-Contrast Modern Serif: `Bodoni Moda` & `Playfair Display` for bold headings (*"PROJECT"*, *"PROBLEM STATEMENT"*, *"WAYVIA MATCH"*).
  - Modern Accessible UI Sans: `Plus Jakarta Sans`.
- **Scrapbook / Stationery Design Details**:
  - Metallic sky-blue paperclips clipping cards to the striped background.
  - Blue & white gingham washi tape angled across card corners.
  - Scalloped stamp/cloud card containers with hot-pink (`#E83D84`) dashed borders.
  - Deep blue location pins (`#1E40AF`) with curved dashed journey lines (`- - - -`).
  - **No generic purple AI gradients** or impersonal SaaS dashboard patterns.

---

## 🚀 Google Technologies in WAYVIA

WAYVIA visibly incorporates Google's ecosystem at every step of the user journey:

1. **Gemini NLU & Extraction**:
   - Parses complex conversational prompts (e.g., *"Find me a quiet vegetarian café with wheelchair access and parking within 3 km"*) into structured criteria chips:
     - `Category: Café`
     - `Mobility: Wheelchair accessible entrance, Step-free interior`
     - `Dietary: Vegetarian`
     - `Environment: Quiet (< 55 dB)`
     - `Parking: Dedicated van stalls`
     - `Radius: Within 3 km`
2. **Google Maps Platform**:
   - Interactive vector map layer with custom WAYVIA accessibility pins.
   - Synchronized place selection, user location centering, and travel journey trails.
   - Live external deep-links to `Get Directions` and `View on Google Maps`.
3. **Google Places API (New)**:
   - High-fidelity place metadata and accessibility fields:
     - Wheelchair-accessible entrance
     - Wheelchair-accessible parking
     - Wheelchair-accessible restroom
     - Wheelchair-accessible seating
   - Attribution: *"Information from Google Maps"*.
4. **Grounding with Google Maps**:
   - *Ask WAYVIA* AI Assistant grounds recommendations directly on Places data and attributes: *"Grounded with Google Maps & Places API (New)"*.
5. **Firebase / Firebase AI Logic Ready**:
   - Clean modular service layer prepared for cloud deployment and live API key configuration.

---

## 🛡️ The 3-State Accessibility Paradigm

WAYVIA never makes dangerous assumptions about accessibility:
- **`✓ VERIFIED`**: Confirmed by Google Maps attributes, facility measurements, or official audits.
- **`? UNKNOWN / NOT VERIFIED`**: Data is unavailable or pending re-verification. **Unknown is never penalized as negative**; it is transparently surfaced with guidance to call ahead.
- **`✕ DOESN'T MATCH`**: Known physical barriers or direct conflicts with the user's active requirements (e.g., entrance steps with no ramp).

---

## 🗺️ Key Screens & Features

| View | Description |
|---|---|
| **Landing Page** | Hero banner with *"Find Your Way. Your Way."*, 4-step journey cards, Google technology strip, and the Team Vertex Problem Statement card with paperclip & washi tape. |
| **Dashboard** | Natural-language Gemini search bar with live extraction animation, Accessibility Insights (*"3 nearby restaurants match your mobility preferences"*), and ranked place cards. |
| **Explore** | Dual-mode view: **List View** & **Interactive Google Maps View** with search, category tabs, and real-time pin synchronization. |
| **Categories** | 8 destination categories (Cafés, Restaurants, Hospitals, Hotels, Shopping, Parks, Entertainment, Public Services). |
| **Place Details** | The signature screen: Hero gallery, WAYVIA Match Ring (`92% Match`), **Know Before You Go** (Verified, Unknown, Doesn't Match), dynamic *"Why this place matches you"*, categorized Accessibility Overview, and Google Places data attribution. |
| **Ask WAYVIA** | Intelligent location assistant grounded in Google Maps with pre-loaded prompts and structured venue cards. |
| **Compare** | Side-by-side comparative matrix of 2–3 venues across entrance, restrooms, parking, noise level, and suitability scores. |
| **My WAYVIA Profile** | Interactive mobility, sensory, dietary, and parking preferences (`Required ✓`, `Preferred ✦`, `Not Important`). Modifying settings **dynamically recalculates match percentages across the entire app in real time**! |
| **Saved Places** | Persistent bookmarking of venues with quick directions, compare triggers, and verification status. |
| **Report an Update** | Community reporting modal to audit entrance, restroom, or seating changes with clear disclaimer that user reports are submitted for review. |
| **Section 23 Guided Demo** | Interactive 8-step guided tour walking judges through the complete user journey. |

---

## 💻 Running the Application

The web application is already running locally on port **5173**.

To start or restart the server manually:

```powershell
cd C:\Users\byris\.gemini\antigravity\scratch\wayvia
python server.py
```

Then open your browser at:
**[http://localhost:5173](http://localhost:5173)**

---

*“Google Maps helps me find the place. WAYVIA helps me understand whether that place works for me.”*

import pandas as pd

# Initialize list to hold data
data = []

# Helper function to add rows
def add_row(group, category, term, definition, characteristics, relevance):
    data.append({
        "Group": group,
        "Category": category,
        "Term": term,
        "Definition": definition,
        "Characteristics/Range": characteristics,
        "Relevance to Home/Harassment": relevance
    })

# --- 1. NOISE TYPES (Expanded) ---
g = "Audio/Sound"
c = "Noise Types"
add_row(g, c, "White Noise", "Random signal with equal intensity at constant bandwidth.", "Flat spectrum.", "Masking, static hiss. Can cause fatigue/disorientation.")
add_row(g, c, "Pink Noise", "Equal energy per octave (1/f noise).", "-3dB/octave.", "Sounds like rushing water. Used for room EQ. Less harsh than white.")
add_row(g, c, "Brownian (Red) Noise", "Random signal mimicking Brownian motion.", "-6dB/octave (Low freq bias).", "Deep rumble, thunder. Hard to block; mimics heavy machinery.")
add_row(g, c, "Blue (Azure) Noise", "Energy increases with frequency.", "+3dB/octave.", "Hissing, piercing. Very annoying/fatiguing.")
add_row(g, c, "Violet (Purple) Noise", "Differentiation of white noise.", "+6dB/octave.", "Extremely high pitched hiss; irritating.")
add_row(g, c, "Grey Noise", "Psychoacoustically modified white noise.", "Equal loudness curve.", "Perceived as 'flat' volume across spectrum.")
add_row(g, c, "Green Noise", "Mid-range frequency noise.", "500Hz-2kHz focus.", "Ambient nature sound. Generally less harassing, used for masking.")
add_row(g, c, "Black Noise", "Silence or noise with a 1/f^beta spectrum (beta > 2).", "Near silence or erratic spikes.", "Sudden drops in pressure or 'dead' silence can be disorienting.")
add_row(g, c, "Impulse Noise", "Sudden bursts of high-level noise.", "Short duration, high peak.", "Banging, slamming, popping. Causes startle response/anxiety.")
add_row(g, c, "Tonal Noise", "Noise with a distinct pitch or hum.", "Narrow bandwidth peak.", "Transformer hum, whine. Highly intrusive due to constant pitch.")
add_row(g, c, "Broadband Noise", "Noise distributed over a wide frequency range.", "Wide spectrum.", "Vacuum cleaners, HVAC airflow. General masking.")
add_row(g, c, "Narrowband Noise", "Noise concentrated in a narrow frequency range.", "Limited bandwidth.", "Specific whining sounds, whistling.")
add_row(g, c, "Structure-borne Noise", "Vibration transmitted through solid building elements.", "Low frequency dominance.", "Footsteps, impact sounds. Becomes airborne sound in the victim's room.")
add_row(g, c, "Airborne Noise", "Sound transmitted directly through the air.", "Mid-High frequencies.", "Voices, TV, music entering through windows/cracks.")
add_row(g, c, "Intermittent Noise", "Noise that stops and starts.", "Unpredictable intervals.", "Harder to habituate to than constant noise; disrupts concentration/sleep.")

# --- 2. SOUND SPECTRUM & FREQUENCY (Expanded) ---
c = "Sound Spectrum"
add_row(g, c, "Infrasound", "Sound below human hearing threshold.", "< 20 Hz.", "Causes fear, nausea, vibration, 'ghostly' feelings. Penetrates walls.")
add_row(g, c, "Audible Sound", "Standard hearing range.", "20 Hz - 20 kHz.", "Standard speech and music range.")
add_row(g, c, "Ultrasound", "Sound above human hearing threshold.", "> 20 kHz.", "Directional beam. Can cause headaches, ear pressure, heating.")
add_row(g, c, "Hypersound", "Extremely high frequency sound.", "> 100 MHz.", "Used in medical imaging; unlikely in home harassment but physically possible.")
add_row(g, c, "Mosquito Tone", "High freq tone audible to youth.", "~17.4 kHz.", "Used for age-specific harassment or dispersal.")
add_row(g, c, "The Hum", "Persistent low-frequency invasive droning.", "Variable low freq.", "Source of distress; often internal or environmental resonance.")
add_row(g, c, "Sub-bass", "Very low audio frequencies.", "20 Hz - 60 Hz.", "Felt physically in the chest/body. Thumping music/machinery.")
add_row(g, c, "Mid-Range", "Frequencies most sensitive to human ear.", "250 Hz - 4 kHz.", "Speech intelligibility range. Most annoying range for distracting speech.")
add_row(g, c, "Presence Range", "Frequencies providing clarity/closeness.", "4 kHz - 6 kHz.", "Boosts perception of a sound being 'near' or 'in the ear'.")
add_row(g, c, "Brilliance", "High frequency harmonics.", "6 kHz - 20 kHz.", "Adds 'air' or hiss to sounds.")

# --- 3. WAVEFORMS & SYNTHESIS (Expanded) ---
c = "Waveforms"
add_row(g, c, "Sine Wave", "Purest waveform, single frequency.", "No harmonics.", "Tinnitus-like tone. Electrical mains hum (pure).")
add_row(g, c, "Square Wave", "Alternating instantaneous high/low.", "Odd harmonics (harsh).", "Digital alarms, aggressive buzzing.")
add_row(g, c, "Triangle Wave", "Linear rise and fall.", "Odd harmonics (softer).", "Flute-like alarm. Softer than square.")
add_row(g, c, "Sawtooth Wave", "Ramp up and sharp drop.", "All harmonics (buzzy).", "Motor/engine sounds, electric buzzing.")
add_row(g, c, "Pulse Wave", "Rectangular wave with variable width.", "Variable harmonics.", "Switching noise, digital data streams.")
add_row(g, c, "PWM (Pulse Width Modulation)", "Encoding analog signal into pulse widths.", "Duty cycle variation.", "Motor controllers, LED dimmers (can sing/whine).")
add_row(g, c, "Complex Waveform", "Combination of multiple simple waves.", "Varied.", "Real-world sounds (speech, music).")
add_row(g, c, "Chirp", "Signal in which frequency increases/decreases with time.", "Sweeping freq.", "Radar, sonar, testing room acoustics (sweeps).")

# --- 4. ACOUSTICS & PHYSICS (Expanded) ---
g = "Physics/Environment"
c = "Acoustics"
add_row(g, c, "Resonance", "Tendency to vibrate at specific frequencies.", "System specific.", "Objects/rooms humming sympathetically.")
add_row(g, c, "Standing Wave", "Wave remains in constant position due to interference.", "Nodes/Antinodes.", "Uneven volume distribution in room (loud/quiet spots).")
add_row(g, c, "Room Modes", "Resonances specific to room dimensions.", "Low frequencies.", "Bass booming in corners. Can mimic directional harassment.")
add_row(g, c, "Reverberation (RT60)", "Sound persistence after source stops.", "Time decay.", "Muddy audio, confusion.")
add_row(g, c, "Diffraction", "Bending of waves around obstacles.", "Wavelength dependent.", "Low bass bending around corners/walls.")
add_row(g, c, "Refraction", "Bending of waves due to medium speed change.", "Temp gradients.", "Sound carrying further at night due to temp inversion.")
add_row(g, c, "Constructive Interference", "Waves combine to increase amplitude.", "Louder volume.", "Multiple sources creating a 'hot spot'.")
add_row(g, c, "Destructive Interference", "Waves combine to cancel out.", "Silence.", "Dead zones.")
add_row(g, c, "Beat Frequency", "Pulsing from two similar frequencies.", "Difference (f1-f2).", "Wobbly, throbbing sound (e.g., fans running at slightly diff speeds).")
add_row(g, c, "Doppler Effect", "Frequency change due to motion.", "Pitch shift.", "Passing vehicles, or simulated motion.")
add_row(g, c, "Sound Transmission Class (STC)", "Rating of how well a partition attenuates sound.", "Airborne loss.", "Rating walls for privacy.")
add_row(g, c, "Impact Insulation Class (IIC)", "Rating of floor/ceiling impact noise.", "Impact loss.", "Footsteps/dragging noise insulation.")
add_row(g, c, "Flanking Transmission", "Sound bypassing the primary barrier.", "Ducts/Vents.", "Hearing neighbors through vents despite thick walls.")
add_row(g, c, "Coincidence Effect", "Panel vibrates easily at specific freq/angle.", "Transparency dip.", "Wall becoming 'transparent' to sound at certain pitch.")

# --- 5. PSYCHOACOUSTICS & PERCEPTION (Expanded) ---
g = "Perception/Health"
c = "Psychoacoustics"
add_row(g, c, "Binaural Beats", "Illusion from two diff tones in each ear.", "Brain entrainment.", "Inducing relaxation or anxiety.")
add_row(g, c, "Shepard Tone", "Illusion of infinitely rising/falling pitch.", "Superimposed octaves.", "Creates tension/anxiety.")
add_row(g, c, "Haas Effect (Precedence)", "Localization dominated by first arrival.", "<40ms delay.", "Confuses source location.")
add_row(g, c, "Cocktail Party Effect", "Focusing on one voice in noise.", "Selective attention.", "Harassment often targets this ability (distraction).")
add_row(g, c, "Masking", "One sound hiding another.", "Freq dependent.", "Using noise to hide speech.")
add_row(g, c, "Hyperacusis", "Painful sensitivity to sound.", "Reduced tolerance.", "Everyday sounds become unbearable.")
add_row(g, c, "Misophonia", "Emotional rage at specific sounds.", "Trigger specific.", "Eating/tapping noises trigger fight/flight.")
add_row(g, c, "Tinnitus", "Ringing in ears.", "Subjective.", "Can be induced by high SPL or stress.")
add_row(g, c, "Phonophobia", "Fear of loud sounds.", "Psychological.", "Anticipatory anxiety regarding noise.")
add_row(g, c, "Phantom Fundamental", "Hearing a low pitch that isn't there.", "Harmonic inference.", "Brain reconstructs missing bass from harmonics.")
add_row(g, c, "Auditory Pareidolia", "Hearing voices/patterns in random noise.", "Pattern matching.", "Hearing 'voices' in fans or white noise.")

# --- 6. BIOLOGICAL & HEALTH EFFECTS (New Category) ---
c = "Bio-Effects"
add_row(g, c, "Vibroacoustic Disease", "Pathology from long-term low freq noise.", "Tissue thickening.", "Health consequence of chronic infrasound.")
add_row(g, c, "Whole Body Vibration", "Shaking of entire body.", "0.5 Hz - 80 Hz.", "Nausea, fatigue, back pain.")
add_row(g, c, "Visceral Resonance", "Internal organs vibrating.", "5 Hz - 20 Hz.", "Eyeballs (18Hz), Chest wall (60Hz).")
add_row(g, c, "Sleep Architecture Disruption", "Noise affecting sleep stages.", "REM/Deep sleep.", "Chronic fatigue, brain fog.")
add_row(g, c, "Startle Reflex", "Involuntary reaction to sudden noise.", "Brainstem.", "Increased cortisol, heart rate.")
add_row(g, c, "Threshold Shift (TTS/PTS)", "Hearing loss.", "dB level.", "Temporary or permanent damage from loud noise.")

# --- 7. MEASUREMENT & ANALYSIS (Expanded) ---
g = "Measurement"
c = "Units/Analysis"
add_row(g, c, "Decibel (dB)", "Logarithmic unit of intensity.", "Ratio.", "Basic volume measure.")
add_row(g, c, "dBA (A-weighted)", "Human hearing adjustment.", "Filters bass.", "Standard legal measure (often misses low freq harassment).")
add_row(g, c, "dBC (C-weighted)", "Flatter response.", "Includes bass.", "Better for measuring bass noise/vibration.")
add_row(g, c, "dBZ (Z-weighted)", "Zero weighting (flat).", "Raw data.", "Scientific measurement.")
add_row(g, c, "Leq (Equivalent Level)", "Average sound energy over time.", "Time average.", "Measures total exposure.")
add_row(g, c, "Lmax/Lmin", "Max and Min levels.", "Extremes.", "Captures peak harassment events.")
add_row(g, c, "Spectrum Analyzer", "Visualizes amplitude vs frequency.", "Graph.", "Identifies specific tones.")
add_row(g, c, "Spectrogram", "Frequency vs Time waterfall.", "Visual pattern.", "Shows patterns/cycles of harassment.")
add_row(g, c, "FFT (Fast Fourier Transform)", "Algorithm to analyze freqs.", "Math processing.", "Converting audio to frequency data.")
add_row(g, c, "Noise Floor", "Background noise level.", "Base dB.", "Silence level.")
add_row(g, c, "Crest Factor", "Ratio of peak to RMS.", "Dynamics.", "High crest factor = impulsive (banging).")

# --- 8. HARDWARE: EMITTERS (Expanded) ---
g = "Hardware"
c = "Emitters"
add_row(g, c, "Subwoofer", "Low frequency speaker.", "20-200 Hz.", "Thumping, vibration source.")
add_row(g, c, "Tweeter", "High frequency speaker.", "2k-20k Hz.", "Piercing highs.")
add_row(g, c, "Parametric Speaker (LRAD)", "Directional ultrasound beam.", "Ultrasonic carrier.", "Audio Spotlight: 'Voice in head' effect.")
add_row(g, c, "Tactile Transducer (Shaker)", "Vibrates surfaces directly.", "Physical coupling.", "Turns walls/floors into speakers.")
add_row(g, c, "Signal Generator", "Creates electronic waveforms.", "Synth.", "Source of test tones/harassment.")
add_row(g, c, "Piezo Buzzer", "Cheap high-pitch emitter.", "Resonant.", "Annoying beeps in hidden devices.")
add_row(g, c, "Bone Conduction Transducer", "Transmits via skull.", "Vibration.", "Bypasses ears.")
add_row(g, c, "Mosquito Device", "Anti-loitering high freq emitter.", "17kHz.", "Harassment tool for youth/sensitive adults.")

# --- 9. HARDWARE: RECEIVERS/DETECTORS (New Category) ---
c = "Receivers/Detectors"
add_row(g, c, "Condenser Microphone", "Sensitive, accurate mic.", "High fidelity.", "Good for recording evidence.")
add_row(g, c, "Dynamic Microphone", "Rugged mic.", "Lower sensitivity.", "Less likely to pick up subtle distant noise.")
add_row(g, c, "Contact Microphone", "Senses vibration in solids.", "Piezo element.", "Detects wall vibrations not audible in air.")
add_row(g, c, "Accelerometer", "Measures physical vibration/g-force.", "Vibration sensor.", "Proving floor/wall shaking.")
add_row(g, c, "Geophone", "Earthquake/ground sensor.", "Seismic.", "Detecting extremely low freq earth/structure vibration.")
add_row(g, c, "Parabolic Mic", "Focused long-range mic.", "Dish reflector.", "Spying/Listening from distance.")
add_row(g, c, "Laser Doppler Vibrometer", "Measures surface vibration with laser.", "Optical.", "Remote listening to window vibrations.")
add_row(g, c, "RF Detector", "Detects radio signals.", "EMF.", "Finding hidden bugs or transmission sources.")

# --- 10. EMF, EMI & SIGNALS (Expanded) ---
g = "EMF/Signal"
c = "Electromagnetics"
add_row(g, c, "Mains Hum", "Electrical grid noise.", "50/60 Hz.", "Constant drone.")
add_row(g, c, "EMI (Electromagnetic Interference)", "Induction into circuits.", "Broadband.", "Buzzing in speakers.")
add_row(g, c, "RFI (Radio Frequency Interference)", "Radio affecting electronics.", "High freq.", "Hearing radio stations in powered speakers.")
add_row(g, c, "Dirty Electricity", "Voltage transients on wiring.", "Harmonics.", "Buzzing, biological stress.")
add_row(g, c, "Ground Loop", "Current between ground points.", "Hum.", "Loud buzzing in audio gear.")
add_row(g, c, "Carrier Wave", "Modulated transport wave.", "RF/Ultrasound.", "Hidden audio transport.")
add_row(g, c, "Amplitude Modulation (AM)", "Volume modulation.", "Envelope.", "Encoding audio.")
add_row(g, c, "Frequency Modulation (FM)", "Pitch modulation.", "Vibrato.", "Encoding audio.")
add_row(g, c, "Frey Effect (Microwave Hearing)", "Pulsed RF perception.", "Thermal expansion.", "Clicks/buzzing inside head from RF.")
add_row(g, c, "Demodulation", "Extracting audio from carrier.", "Detection.", "Hearing the message.")
add_row(g, c, "Heterodyning", "Mixing freqs to create new ones.", "Beat freqs.", "Shifting ultrasound down to audible range.")

# --- 11. LEGAL & INVESTIGATION (Expanded) ---
g = "Context"
c = "Legal/Investigative"
add_row(g, c, "Quiet Enjoyment", "Right to peace in home.", "Legal covenant.", "Basis for lawsuits.")
add_row(g, c, "Private Nuisance", "Interference with land use.", "Tort.", "Civil claim.")
add_row(g, c, "Breach of Peace", "Disorderly conduct.", "Criminal.", "Police matter.")
add_row(g, c, "Chain of Custody", "Evidence handling documentation.", "Legal process.", "Ensuring recordings are admissible.")
add_row(g, c, "Calibration", "Verifying measurement accuracy.", "Standardization.", "Proof that meter readings are correct.")
add_row(g, c, "Log/Diary", "Written record of events.", "Corroboration.", "Matching recordings to subjective experience.")
add_row(g, c, "Gaslighting", "Psychological manipulation.", "Abuse.", "Denying reality of harassment.")
add_row(g, c, "Electronic Harassment", "Use of tech to harass.", "Cyber/Physical.", "Modern legal category.")
add_row(g, c, "Counter-surveillance", "Detecting surveillance.", "Defense.", "Sweeping for bugs.")

# Create DF
df_comprehensive = pd.DataFrame(data)

# Display info
print(f"Total Rows: {len(df_comprehensive)}")
print(df_comprehensive['Category'].value_counts())

# Save
df_comprehensive.to_csv('Comprehensive_Audio_Harassment_Terms.csv', index=False)

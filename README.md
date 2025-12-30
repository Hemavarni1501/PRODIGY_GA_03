# GA_03: Text Generation with Markov Chains

## 🔗 Project Link
* **Live Application:** [Markov Text Generation Engine](https://appigyga03-nuqpsd649xxiavqtfqeemi.streamlit.app/)

---

## 📌 Project Overview
Developed as part of the **Prodigy Infotech** Generative AI internship, this project implements a **Markov Chain** algorithm for statistical text synthesis. Unlike modern Transformer-based LLMs, this system utilizes a stochastic process to predict the probability of a character or word based solely on the previous state (N-gram).



## 🛠️ Technical Implementation
* **Algorithm:** Custom-built `MarkovGenerator` class utilizing Python dictionaries for $O(1)$ complexity lookups.
* **N-gram Modeling:** Supports 1st, 2nd, and 3rd-order chains, allowing users to tune the balance between creative randomness and structural coherence.
* **State Management:** Leveraged `st.session_state` and callback functions to provide a seamless, instant "Sample Data" loading experience.
* **Interface:** Streamlit-based UI designed for iterative testing and real-time visualization of the generation process.

## 🚀 Key Engineering Features
1. **Dynamic Corpus Training:** The model tokenizes and builds a probability map in real-time from any user-provided text (news, literature, or technical papers).
2. **Seed Word Logic:** Integrated a starting-state mechanism that allows the user to guide the direction of the generated text.
3. **Instant Testing:** Added a "Load Sample Data" feature to allow recruiters and reviewers to verify the model's logic with one click without needing an external dataset.

## 📁 Installation & Local Setup
To run this project locally:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Hemavarni1501/PRODIGY_GA_03.git](https://github.com/Hemavarni1501/PRODIGY_GA_03.git)
   cd PRODIGY_GA_03
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the application:**
   ```bash
   streamlit run app.py
   ```

## 📊 Results Summary
The system successfully demonstrates the fundamentals of predictive text. By increasing the Model Order, the output transitions from "word salad" (1st order) to grammatically plausible sentences (3rd order), effectively satisfying the internship requirement for a statistical prediction model.

#### Internship: Prodigy Infotech

#### Track: Generative AI

#### Task: 03

#### Developer: Hemavarni.S

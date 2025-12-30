import streamlit as st
import random
import re

# 1. System UI Configuration
st.set_page_config(page_title="Text Generation with Markov Chains", layout="centered")

# --- Sample Data for testing ---
SAMPLE_CORPUS = """The future of Generative AI is bright and full of potential. 
Artificial Intelligence is not just about automation; it is about human-centric creativity. 
As we build smarter models, we must focus on ethical AI and data privacy. 
Technology moves fast, but the principles of good engineering remain the same. 
A Markov Chain is a simple yet powerful statistical model used in natural language processing. 
It predicts the next state based solely on the current state, creating a sequence of probable outcomes."""

# --- Callback function to update the text area instantly ---
def load_sample():
    st.session_state.corpus_input = SAMPLE_CORPUS

class MarkovGenerator:
    def __init__(self, order=1):
        self.order = order
        self.lookup_dict = {}

    def train(self, text):
        # Tokenize text into words
        words = re.findall(r'\b\w+\b', text.lower())
        if len(words) <= self.order:
            return False
            
        for i in range(len(words) - self.order):
            state = tuple(words[i : i + self.order])
            next_word = words[i + self.order]
            
            if state not in self.lookup_dict:
                self.lookup_dict[state] = []
            self.lookup_dict[state].append(next_word)
        return True

    def generate(self, length=30, seed=None):
        if not self.lookup_dict:
            return "Model not trained."

        if seed and tuple(seed.lower().split()) in self.lookup_dict:
            state = tuple(seed.lower().split())
        else:
            state = random.choice(list(self.lookup_dict.keys()))

        result = list(state)
        for _ in range(length):
            next_options = self.lookup_dict.get(state)
            if not next_options:
                break
            next_word = random.choice(next_options)
            result.append(next_word)
            state = tuple(result[-self.order:])
            
        return " ".join(result).capitalize() + "."

# 2. Main UI Header
st.title("Text Generation with Markov Chains")
st.caption("PRODIGY INFOTECH | TRACK: GA | TASK: 03")
st.markdown("---")

# 3. Training Phase (Old UI Layout)
st.subheader("1. Training Phase")

# Extra button to load sample data
st.button("📝 Load Sample Data", on_click=load_sample, help="Click to pre-fill with sample text for testing.")

corpus = st.text_area(
    "Input Training Corpus", 
    height=200,
    placeholder="Paste your training text here...",
    key="corpus_input", # This key binds the text area to the callback
    help="The model learns probabilities from this text."
)

# 4. Configuration Section (Old UI Layout)
st.subheader("2. Generation Parameters")
col1, col2 = st.columns(2)
with col1:
    order = st.select_slider("Model Order (N-gram)", options=[1, 2, 3], value=1)
with col2:
    length = st.number_input("Max Words", min_value=5, max_value=200, value=30)

seed_word = st.text_input("Start Word (Optional)", placeholder="e.g. AI")

# 5. Execution Logic
if st.button("🚀 EXECUTE SYNTHESIS", type="primary"):
    if not corpus.strip():
        st.error("❌ Error: Training corpus cannot be empty.")
    else:
        with st.spinner("Analyzing patterns..."):
            model = MarkovGenerator(order=order)
            if model.train(corpus):
                output = model.generate(length=length, seed=seed_word if seed_word else None)
                st.markdown("---")
                st.write("**Generated Text Output:**")
                st.success(output)
            else:
                st.error("❌ Error: Text is too short for the selected Model Order.")
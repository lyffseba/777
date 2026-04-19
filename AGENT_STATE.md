# 🤖 ENTS - Continuous Development State
> *This file is used to hand off context and next steps between AI coding sessions.*

## Current Status (2026-04-18)
- **Project Goal:** Building a from-scratch AI inference engine (`ents`) focusing on the evolutionary history of LLMs (from Bigram up to GPT-2/3), themed around the **Ents of Middle-earth** 🌳.
- **Environment:** Pixi is set up in `max_env` with `max`, `modular`, `jax`, `flax`, and `onnx`.
- **Milestones Achieved:**
  - Designed the "Tri-Force" Architecture (JAX -> MAX -> Mojo) mapping out the journey.
  - Downloaded the "Young Ent" GPT-2 (124M parameter) ONNX model to `max_env/models/gpt2/`.
  - Configured Hugging Face sync and set `.gitignore` to safely handle large weights.

## Repository Sync Note
- The main code (Pixi files, `src`, `scripts`) is now properly tracked in Git. The `.pixi/` environments are ignored.
- **To sync to Hugging Face:** `git push hf main`
- **To sync to GitHub:** `git push origin main` (User needs to fix local github credentials for `lyffseba`)

## 🚀 NEXT STEPS FOR THE AGENT
1. **Kickoff Phase 1 (The Seed/Bigram):** Write a simple Bigram language model in JAX to establish the math, then implement the exact same lookup logic in a bare-metal Mojo file (`bigram.mojo`).
2. **Compile GPT-2 (Python):** (Parallel track) Create `run_gpt2.py` to compile `models/gpt2/onnx/decoder_model.onnx` using `max.engine.InferenceSession`.
3. **Execute Inference (Python):** Pass dummy tokens (e.g., `[[15496, 11, 314]]`) through the model and print the logits shape.
4. **Implement Tokenizer:** Add a basic BPE tokenizer to convert real text strings to tokens and back.

---
*Agent Instructions:* When starting a new session, read this file to understand where the project left off. When completing a task, update the "Current Status" and "Next Steps" sections accordingly.
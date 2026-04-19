# 🤖 GEMAX - Continuous Development State
> *This file is used to hand off context and next steps between AI coding sessions.*

## Current Status (2026-04-18)
- **Project Goal:** Building a from-scratch AI inference engine (`gemax`) using Modular MAX, Mojo, and Pixi, specifically focusing on building a **GPT-2** implementation (inspired by Andrej Karpathy's `nanoGPT`/`llm.c` approaches).
- **Environment:** Pixi is set up in `max_env` with `max`, `modular`, and `huggingface_hub` dependencies.
- **Milestones Achieved:**
  - Initialized Modular MAX engine and successfully loaded Apple Silicon GPU (`Device(type=gpu,id=0)`).
  - Configured Hugging Face integration (`hf` CLI authenticated).
  - Downloaded the GPT-2 (124M parameter) ONNX model to `max_env/models/gpt2/`.

## Repository Sync Note
- The main code (Pixi files, `src`, `scripts`) is now properly tracked in Git. The `.pixi/` environments are ignored.
- **To sync to Hugging Face:** `git push hf main`
- **To sync to GitHub:** `git push origin main` (User needs to fix local github credentials for `lyffseba`)

## 🚀 NEXT STEPS FOR THE AGENT
1. **Model Acquisition:** *(DONE)* Downloaded GPT-2 ONNX model.
2. **Compile GPT-2 (Python):** Create `run_gpt2.py` to compile `models/gpt2/onnx/decoder_model.onnx` using `max.engine.InferenceSession`.
3. **Execute Inference (Python):** Pass dummy tokens (e.g., `[[15496, 11, 314]]`) through the model and print the logits shape (should match `[batch, sequence_length, vocab_size]`).
4. **Implement Tokenizer:** Add a basic GPT-2 BPE tokenizer to convert real text strings to tokens and back.
5. **Transition to Mojo:** Once the forward pass works in Python, write the equivalent graph compilation and inference logic in Mojo.

---
*Agent Instructions:* When starting a new session, read this file to understand where the project left off. When completing a task, update the "Current Status" and "Next Steps" sections accordingly.
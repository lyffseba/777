# 🤖 GEMAX - Continuous Development State
> *This file is used to hand off context and next steps between AI coding sessions.*

## Current Status (2026-04-18)
- **Project Goal:** Building a from-scratch AI inference engine (`gemax`) using Modular MAX, Mojo, and Pixi.
- **Environment:** Pixi is set up in `max_env` with `max`, `modular`, and `huggingface_hub` dependencies.
- **Milestones Achieved:**
  - Initialized Modular MAX engine and successfully loaded Apple Silicon GPU (`Device(type=gpu,id=0)`).
  - Renamed the project from `gm4x` to `gemax`.
  - Configured Hugging Face integration (`hf` CLI authenticated).
  - Created an automated upload script (`max_env/scripts/upload_to_hf.py`).
  - Synced to Hugging Face repo (`lyffseba/gemax`). GitHub push is pending due to a local `403` credential error.

## Repository Sync Note
- The main code (Pixi files, `src`, `scripts`) is now properly tracked in Git. The `.pixi/` environments are ignored.
- **To sync to Hugging Face:** `git push hf main`
- **To sync to GitHub:** `git push origin main` (User needs to fix local github credentials for `lyffseba`)

## 🚀 NEXT STEPS FOR THE AGENT
1. **Model Acquisition:** Download a small, fast ONNX model (e.g., MobileNet or a simple text/embedding model) into `max_env/models/`.
2. **Compile Model (Python):** Update `check_engine.py` (or create `run_inference.py`) to compile the downloaded model using the `max.engine.InferenceSession`.
3. **Execute Inference (Python):** Pass dummy or sample input data through the model and print the shape/values of the output tensors.
4. **Transition to Mojo:** Once the Python baseline runs successfully, begin porting the inference logic into a `.mojo` file.

---
*Agent Instructions:* When starting a new session, read this file to understand where the project left off. When completing a task, update the "Current Status" and "Next Steps" sections accordingly.
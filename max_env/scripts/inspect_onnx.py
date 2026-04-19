import onnx

def main():
    model_path = "models/gpt2/onnx/decoder_model.onnx"
    model = onnx.load(model_path, load_external_data=False)
    print("Inputs:")
    for input in model.graph.input:
        print(f" - {input.name}: {input.type.tensor_type.elem_type} (shape: {[dim.dim_value for dim in input.type.tensor_type.shape.dim]})")
    print("Outputs:")
    for output in model.graph.output:
        print(f" - {output.name}: {output.type.tensor_type.elem_type} (shape: {[dim.dim_value for dim in output.type.tensor_type.shape.dim]})")

if __name__ == "__main__":
    main()

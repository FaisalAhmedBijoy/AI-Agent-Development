from transformers import AutoModelForCausalLM, AutoTokenizer

class LlamaAgent:
    def __init__(self, model_name="meta-llama/Llama-3.2-1B-Instruct"):
        """
        Initialize the Llama model and tokenizer.
        """
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            device_map="auto",
            torch_dtype="float16"
        )

    def query_llama(self, prompt):
        """
        Generate a response from the Llama model.
        """
        inputs = self.tokenizer(prompt, return_tensors="pt").to("cuda")
        outputs = self.model.generate(
            **inputs,
            max_length=256,
            temperature=0.7,
            top_p=0.9
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response


agent = LlamaAgent()
print('agent: ',agent)
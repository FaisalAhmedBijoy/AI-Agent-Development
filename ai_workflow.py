import json

class AIWorkflow:
    def __init__(self, model_name="meta-llama/Llama-2-7b-chat-hf"):
        self.llama_agent = LlamaAgent(model_name)

    def process_command(self, command):
        """
        Use the Llama model to understand the user's command and extract entities.
        """
        prompt = f"""
        You are an AI assistant for an ERP system. Process the following command:
        
        Command: "{command}"
        
        1. Identify the intent (e.g., 'money_request').
        2. Extract relevant entities such as 'amount' and 'recipient'.
        3. Respond in JSON format like:
        {{
            "intent": "<intent>",
            "entities": {{
                "amount": <amount>,
                "recipient": "<recipient>"
            }}
        }}
        """
        response = self.llama_agent.query_llama(prompt)

        # Convert Llama's response into a dictionary
        try:
            parsed_response = json.loads(response)
        except json.JSONDecodeError:
            return {"error": "Failed to parse Llama's response."}

        # Validate and process the request
        return self.validate_request(parsed_response)

    def validate_request(self, parsed_response):
        """
        Validate the intent and entities extracted by Llama.
        """
        if "intent" not in parsed_response or "entities" not in parsed_response:
            return {"error": "Invalid response from Llama model."}

        intent = parsed_response["intent"]
        entities = parsed_response["entities"]

        if intent != "money_request":
            return {"error": "Unsupported intent."}

        if entities["amount"] <= 0:
            return {"error": "Amount must be greater than zero."}

        if not entities["recipient"].isalpha():
            return {"error": "Recipient name must contain only letters."}

        # Mock ERP interaction
        return {
            "success": True,
            "message": f"Money request of {entities['amount']} to {entities['recipient']} has been processed."
        }

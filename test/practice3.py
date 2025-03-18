from openai import OpenAI
import os

def generate_text(temperature, max_tokens, scenario, iot_specifications):
    try:
        api_key = os.getenv("OPENAI_API_KEY")
        model_name = "gpt-4o-mini"
        client = OpenAI(
            api_key=api_key,
        )  
        
        messages = [
            {
                "role": "system",
                "content": "You are an expert in optimizing IoT network protocols, analyzing available protocols, and providing the best solution based on resource constraints.",
            },
            {
                "role": "user",
                "content": f"Scenario: {scenario}\nIoT System Specifications: {iot_specifications}",
            },
        ]
        
        response = client.chat.completions.create(
            model=model_name,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens
        )
        
        return response.choices[0].message.content
    
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return None


def test_application():
    scenario = input("Enter the scenario for the network protocol: ")
    iot_specifications = input("Enter the IoT system specifications (e.g., energy, memory constraints): ")
    temperature = float(input("Enter temperature (0.0 - 1.0): "))
    max_tokens = int(input("Enter max tokens: "))
    
    generated_text = generate_text(temperature, max_tokens, scenario, iot_specifications)
    
    if generated_text:
        print(f"Generated Text: {generated_text}")
    else:
        print("Failed to generate text.")

def main():
    print("IoT Network Protocol Optimization and Analysis Tool")
    
    test_application()

if __name__ == "__main__":
    main()
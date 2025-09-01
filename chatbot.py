def chatbot_response(user_input):
    """Simple rule-based chatbot for beginners."""
    responses = {
        "what is rsi": "RSI measures price momentum and can indicate overbought or oversold conditions.",
        "how to start trading": "Start with a trusted exchange, small investments, and risk management.",
        "what is moving average": "A moving average smooths price data to identify trends."
    }
    return responses.get(user_input.lower(), "I'm still learning. Can you rephrase?")

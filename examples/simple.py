from wayfound import Session

wayfound_api_key = "your_wayfound_api_key_here"
wayfound_agent_id = "your_wayfound_agent_id_here"

wayfound_session = Session(wayfound_api_key=wayfound_api_key, agent_id=wayfound_agent_id)

formatted_messages = []

formatted_messages.append({
    "timestamp": "2025-05-07T10:00:00Z",
    "event_type": "assistant_message",
    "attributes": {
      "content": "Hello, how can I help you today?",
    }
  })

formatted_messages.append({
    "timestamp": "2025-05-07T10:00:04Z",
    "event_type": "user_message",
    "attributes": {
      "content": "What's the current status of Project Alpha?"
    }
  })

result = wayfound_session.complete_session(messages=formatted_messages)
print(f"Result: {result}")
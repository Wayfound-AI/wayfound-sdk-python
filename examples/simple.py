from wayfound import Session

wayfound_api_key = "4401f328-b4c2-4f7e-8feb-c85bb8a6f4e3"
wayfound_agent_id = "fb2edb4a-fc1b-4173-ad09-418803041f35"

wayfound_session = Session(wayfound_api_key=wayfound_api_key, agent_id=wayfound_agent_id)

formatted_messages = []

formatted_messages.append({
    "timestamp": "2025-08-07T10:00:00Z",
    "event_type": "assistant_message",
    "attributes": {
      "content": "Hello, how can I help you today?",
    }
  })

formatted_messages.append({
    "timestamp": "2025-08-07T10:00:04Z",
    "event_type": "user_message",
    "attributes": {
      "content": "What's the current status of Project Alpha?"
    }
  })

formatted_messages.append({
    "timestamp": "2025-08-07T10:00:04Z",
    "event_type": "assistant_message",
    "attributes": {
      "content": "The status of Project Alpha is currently on track with all milestones met so far."
    }
  })

print ("Submitting session data to Wayfound...")
result = wayfound_session.complete_session(messages=formatted_messages, is_async=False)

print(f"Status Code: {result.status_code}")
print(f"Response Headers: {dict(result.headers)}")
print(f"Response Body: {result.text}")
print(f"Response JSON: {result.json() if result.headers.get('content-type', '').startswith('application/json') else 'Not JSON'}")

# Find and print compliance violations
response_data = result.json()
session = response_data[0]  # Get first session from the array

print("\n--- Guideline Violations ---")
violations = [item for item in session['compliance'] if item['result']['compliant'] == False]

if violations:
    for i, violation in enumerate(violations, 1):
        print(f"Violation {i}:")
        print(f"  Guideline: {violation['guideline']}")
        print(f"  Reason: {violation['result']['reason']}")
        print(f"  Message: {violation['message']['content']}")
        print(f"  Priority: {violation['guidelinePriority']}")
        print(f"  Source: {violation['guidelineSource']}")
        print()
else:
    print("No guideline violations found!")
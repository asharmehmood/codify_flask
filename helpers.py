import json

class Helpers():
    def __init__(self,):
        pass
    
    def save_feedback_object(self, user_message, api_response, feedback, feedback_text):
        print("Making feedback object")
        feedback_obj ={
            "user_message":user_message,
            "llm_response":api_response,
            "user_feedback":feedback,
            "feedback_text":feedback_text
        }
        
        saved = self.save_data_to_json(feedback_obj)
        
        return saved
    
    def save_data_to_json(self,data):
        print("in saving feedback")
        filename = "codify_feedback.json"
        try:
            # Load existing data from the file
            existing_data = []
            try:
                with open(filename, 'r') as infile:
                    existing_data = json.load(infile)
            except FileNotFoundError:
                pass  # Ignore if the file doesn't exist yet

            # Append the new data
            existing_data.append(data)

            # Write the combined data back to the file
            with open(filename, 'w') as outfile:
                json.dump(existing_data, outfile, indent=4)

            print(f"Feedback data appended and saved to {filename}")
        except Exception as e:
            print(f"Error saving feedback data: {e}")
            return False
            
        return True
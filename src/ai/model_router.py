"""
Multi-Model Router Module
Routes tasks to Gemini, Copilot, or ChatGPT based on workload type
"""

import os


class ModelRouter:
    """
    The ModelRouter acts as the central intelligence hub for Browserx AI,
    delegating tasks to Gemini, Copilot, or ChatGPT based on the workload.
    """
    
    def __init__(self):
        """Initialize the Model Router with available AI engines"""
        self.models = {
            "strategy": "Google Gemini",
            "coding": "Microsoft Copilot",
            "creative": "OpenAI ChatGPT"
        }
        self.active = True
        print(f"[SYSTEM] Model Router active. Council: {list(self.models.values())}")

    def route_task(self, task_type, payload):
        """
        Routes the input payload to the appropriate AI engine.
        
        Args:
            task_type (str): Type of task (strategy, coding, creative, etc.)
            payload (str): The task/query to be processed
            
        Returns:
            str: Routed message with target model
        """
        target = self.models.get(task_type, "General Agent")
        return f"[ROUTED TO {target.upper()}]: Analyzing {payload}..."

    def get_available_models(self):
        """Returns list of available AI models"""
        return self.models

    def set_model_priority(self, task_type, model_name):
        """Update model assignment for a specific task type"""
        if task_type in self.models:
            self.models[task_type] = model_name
            return f"Updated {task_type} routing to {model_name}"
        return f"Task type {task_type} not recognized"

    def enable_router(self):
        """Enable the model router"""
        self.active = True
        return "[SYSTEM] Model Router enabled"

    def disable_router(self):
        """Disable the model router"""
        self.active = False
        return "[SYSTEM] Model Router disabled"


# Global router instance for integration with Browserx core
router = ModelRouter()


# Example usage
if __name__ == "__main__":
    # Show available models
    print(f"Available Models: {router.get_available_models()}")
    
    # Route different task types
    print(router.route_task("strategy", "Analyze market trends"))
    print(router.route_task("coding", "Debug Python syntax error"))
    print(router.route_task("creative", "Generate marketing copy"))
    
    # Update routing
    print(router.set_model_priority("strategy", "OpenAI ChatGPT"))

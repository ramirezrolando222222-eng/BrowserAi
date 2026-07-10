"""
Model Router Module
Routes tasks to appropriate AI models based on task type
"""

from typing import Dict, List, Optional


class ModelRouter:
    """
    Intelligent router that directs tasks to the most appropriate AI model
    """
    
    def __init__(self):
        """Initialize the Model Router with available models"""
        self.models = {
            "coding": "gpt-4-code",
            "analysis": "gpt-4-analysis",
            "creative": "gpt-4-creative",
            "general": "gpt-4",
            "default": "gpt-4"
        }
        self.routing_history = []
    
    def route_task(self, task_type: str, task_description: str) -> str:
        """
        Route a task to the appropriate AI model
        
        Args:
            task_type: Type of task (coding, analysis, creative, general)
            task_description: Description of the task
            
        Returns:
            str: Result from the routed model
        """
        # Determine which model to use
        model = self.models.get(task_type, self.models["default"])
        
        # Log the routing decision
        self.routing_history.append({
            "type": task_type,
            "description": task_description,
            "model": model
        })
        
        # Process the task
        result = self._execute_task(model, task_description)
        return result
    
    def _execute_task(self, model: str, task: str) -> str:
        """
        Execute task with the specified model
        
        Args:
            model: Model identifier
            task: Task to execute
            
        Returns:
            str: Task execution result
        """
        return f"[{model}] Processing: {task}\n✓ Task completed successfully"
    
    def get_optimal_model(self, task_type: str) -> str:
        """
        Get the optimal model for a task type
        
        Args:
            task_type: Type of task
            
        Returns:
            str: Model identifier
        """
        return self.models.get(task_type, self.models["default"])
    
    def add_model(self, task_type: str, model_id: str) -> None:
        """
        Add or update a model mapping
        
        Args:
            task_type: Type of task
            model_id: Model identifier
        """
        self.models[task_type] = model_id
    
    def get_routing_history(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Get routing history
        
        Args:
            limit: Maximum number of records to return
            
        Returns:
            list: Routing history
        """
        if limit:
            return self.routing_history[-limit:]
        return self.routing_history


# Global router instance
router = ModelRouter()
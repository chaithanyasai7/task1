import json
import jsonschema


schema ={
    "type":"object",
    "properties":{
        "id":{"type":"integer"},
        "name":{"type":"string"},
        "age":{"type":"integer"},
        
        "gamesIPlay":{
            "type":"array",
            "items":{"type":"string"},
            "minItems":1,
            "maxItems":2 
            # gamesIPlay will be minimum 1 items and maximum 2 items           
        },
        "hobbiesDetails":{
            "type":"array",
            "items":{
                "type":"object",
                "properties":{
                    "gameName":{"type":"string"},
                    "minPlayers":{"type":"integer"},
                    "maxPlayers":{"type":"integer"}
                },
                # according to gameName iam checking min and max players in both games
                "allOf":[
                    {
                        "if":{
                            "properties":{
                                "gameName":{
                                    "const":"Ludo"

                                }
                            }
                        },
                        "then":{
                            "properties":{
                                "minPlayers":{"const": 2},
                                "maxPlayers":{"const": 4}
                                
                            }
                        }
                    },
                    {
                        "if":{
                            "properties":{
                                "gameName":{
                                    "const":"Cricket"

                                }
                            }
                        },
                        "then":{
                            "properties":{
                                "minPlayers":{"const": 11},
                                "maxPlayers":{"const": 15}

                            }
                        }
                    }
                ]
            }
        },
        "dailySchedule": {
            "type":"array",
            "minItems": 2,
            "allOf":[
                {
                    "contains":{
                        "properties":{
                            "name":{"const":"morning"}
                                                        #    dailySchedule requires morning and night
                        }
                    }
                },
                {
                    "contains":{
                        "properties":{
                            "name":{
                                "const":"night"
                            }
                        }
                    }
                }
            ],
            "items": {
                "type":"object",
                "properties": {
                    "name":{"type":"string"},
                    "tasks": {
                        "type":"array",
                        "minItems": 2,
                        "items":{"type":"string"}
                    }
                },
                "allOf":[
                    {
                        "if":{
                            "properties":{
                                "name":{
                                    "const":"morning"
                                }
                                                                 # And morning requires "brush" and "bath" so,
                            }
                        },"then":{
                            "properties":{
                                "tasks":{
                                    "contains":{
                                        "const":"brush"
                                    }
                                }
                            }
                        }
                        
                    },
                    {
                        "if":{
                            "properties":{
                                "name":{
                                    "const":"morning"
                                }
                            }
                        },"then":{
                            "properties":{
                                "tasks":{
                                    "contains":{
                                        "const":"bath"
                                    }
                                }
                            }
                        }
                        
                    },
                    {
                        "if":{
                            "properties":{
                                "name":{
                                    "const":"night"
                                }
                                                                                          # night requires "walk" and "brush"
                            }
                        },"then":{
                            "properties":{
                                "tasks":{
                                    "contains":{
                                        "const":"walk"
                                    }
                                }
                            }
                        }
                    },
                    {
                        "if":{
                            "properties":{
                                "name":{
                                    "const":"night"
                                }
                            }
                        },"then":{
                            "properties":{
                                "tasks":{
                                    "contains":{
                                        "const":"brush"
                                    }
                                }
                            }
                        }
                    }
                    
                ]               
            
            }
            
        },
        "tasksAccordingToAge":{
            "type":"array",
            "items":{
                "type":"string"
            }}
    },
    "required":["id","name","age"],
        
        
    
    #  id, name, age are required so will write inside the required
          
    "if":{
            "properties":{
                    "age":{
                            "type":"integer",
                            "minimum":18
                    }
            }
            # tasksAccordingToAge either have vote or work if age is greater than 18 so,
    },
    "then":{
        "properties":{
            "tasksAccordingToAge":{
                "type":"array",
                "minItems":1,
                "items":{
                    "enum":["vote","work"]
                }
            }
        }      
                
            

        
    }
}




path = "C:/Users/vadde chaithanya/python pracftice/Task/Task.json"
file = open(path)
data = json.load(file)
validator = jsonschema.Draft7Validator(schema)
errors = validator.iter_errors(data)
error_list =[]
for error in errors:
    error_list.append(error)
    print(error_list)
   

        
        
        

            
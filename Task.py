import json
import jsonschema
schema ={
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "age": {
      "type": "integer"
    },
    "gamesIPlay": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1,
      "maxItems": 2
    },
    "hobbiesDetails": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "gameName": {
            "type": "string"
          },
          "minPlayers": {
            "type": "integer"
          },
          "maxPlayers": {
            "type": "integer"
          }
        },
        "allOf": [
          {
            "if": {
              "properties": {
                "gameName": {
                  "const": "Ludo"
                }
              }
            },
            "then": {
              "properties": {
                "minPlayers": {
                  "const": 2
                },
                "maxPlayers": {
                  "const": 4
                }
              }
            }
          },
          {
            "if": {
              "properties": {
                "gameName": {
                  "const": "Cricket"
                }
              }
            },
            "then": {
              "properties": {
                "minPlayers": {
                  "const": 11
                },
                "maxPlayers": {
                  "const": 15
                }
              }
            }
          }
        ]
      }
    },
    "dailySchedule": {
      "type": "array",
      "minItems": 2,
      "allOf": [
        {
          "contains": {
            "properties": {
              "name": {
                "const": "morning"
              }
            }
          }
        },
        {
          "contains": {
            "properties": {
              "name": {
                "const": "night"
              }
            }
          }
        }
      ],
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string"
          },
          "tasks": {
            "type": "array",
            "minItems": 2,
            "items": {
              "type": "string"
            }
          }
        },
        "allOf": [
          {
            "if": {
              "properties": {
                "name": {
                  "const": "morning"
                }
              }
            },
            "then": {
              "properties": {
                "tasks": {
                  "allOf": [
                    {
                      "contains": {
                        "const": "brush"
                      }
                    },
                    {
                      "contains": {
                        "const": "bath"
                      }
                    }
                  ]
                }
              }
            }
          },
          {
            "if": {
              "properties": {
                "name": {
                  "const": "night"
                }
              }
            },
            "then": {
              "properties": {
                "tasks": {
                  "allOf": [
                    {
                      "contains": {
                        "const": "walk"
                      }
                    },
                    {
                      "contains": {
                        "const": "brush"
                      }
                    }
                  ]
                }
              }
            }
          }
        ]
      }
    },
    "tasksAccordingToAge": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "id",
    "name",
    "age"
  ],
  "if": {
    "properties": {
      "age": {
        "type": "integer",
        "minimum": 18
      }
    }
  },
  "then": {
    "properties": {
      "tasksAccordingToAge": {
        "type": "array",
        "minItems": 1,
        "items": {
          "enum": [
            "vote",
            "work"
          ]
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

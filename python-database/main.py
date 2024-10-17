import mysql.connector
import json 

# Establish connection to the database
mydb = mysql.connector.connect(
    user="root",
    host="localhost",
    database="python_db",
    passwd="root"
)

# Create a cursor object
cur = mydb.cursor()

# Create table (if not already created)
cur.execute("CREATE TABLE IF NOT EXISTS customers (name VARCHAR(255), id INT);")

# Insert data into the table
sql = "INSERT INTO customers (name, id) VALUES (%s, %s)"
values = [
    ("John Doe", 1),
    ("Jane Smith", 2),
    ("Alice Johnson", 3)
]

# Insert each record into the table
cur.executemany(sql, values)


cur.execute("CREATE TABLE IF NOT EXISTS orders (name VARCHAR(255), order_id INT);")

cur.execute("""
    CREATE TABLE IF NOT EXISTS strategies (
        id INT AUTO_INCREMENT PRIMARY KEY,
        strategy_name VARCHAR(50) NOT NULL,
        class VARCHAR(50),
        universe VARCHAR(50) NOT NULL,
        filters JSON
    );
""")

# Your JSON data
strategies = {
    "cruise": {
    "class": "CruiseMomentum",
    "universe": "Mcap_500"
  },
  "finance": {
    "class": None,
    "universe": "Nifty_Finance",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "return_size": 50
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "healthcare": {
    "class": None,
    "universe": "Nifty_Healthcare",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "return_size": 50
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "largecap": {
    "class": None,
    "universe": "Mcap_100",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "return_size": 40
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "positive_return_size": 15
          }
        ]
      }
    ]
  },
  "multicap": {
    "class": None,
    "universe": "Mcap_500",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "return_size": 100
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "positive_return_size": 50
          }
        ]
      }
    ]
  },
  "mnc": {
    "class": None,
    "universe": "Nifty_Mnc",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 1000
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "return_size": 50
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 252,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "risk_tuned_adaptive_etf": {
    "class": None,
    "universe": "Risk_Tuned_Adaptive_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "dynamic_focussed_asset_etf": {
    "class": None,
    "universe": "Dynamic_Focussed_Asset_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "sector_rotation_etf": {
    "class": None,
    "universe": "Sector_Rotation_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "commodities_etf": {
    "class": None,
    "universe": "Commodities_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "intl_etf": {
    "class": None,
    "universe": "Intl_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "factor_etf": {
    "class": None,
    "universe": "Factor_ETF",
    "filters": [
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 2
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 2
          }
        ]
      }
    ]
  },
  "technology_sector": {
    "class": None,
    "universe": "Technology_Sector",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 10
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "financial_sector": {
    "class": None,
    "universe": "Financial_Sector",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 10
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "agricultural_sector": {
    "class": None,
    "universe": "Agricultural_Sector",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 10
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "energy_sector": {
    "class": None,
    "universe": "Energy_Sector",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 10
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 10
          }
        ]
      }
    ]
  },
  "automotive_sector": {
    "class": None,
    "universe": "Automotive_Sector",
    "filters": [
      {
        "filter": "McapFilter",
        "options": [
          {
            "min_market_cap": 2500
          }
        ]
      },
      {
        "filter": "AbsoluteReturnFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "return_size": 10
          }
        ]
      },
      {
        "filter": "PositiveMovementFilter",
        "options": [
          {
            "calendar": "Calendar",
            "lookup_window": 20,
            "positive_return_size": 10
          }
        ]
      }
    ]
  }

  };

# Prepare SQL for inserting data
sql = "INSERT INTO strategies (strategy_name, class, universe, filters) VALUES (%s, %s, %s, %s)"
values = []

# Prepare values to be inserted
for key, value in strategies.items():
    # Convert filters to JSON string if it exists
    filters_json = json.dumps(value.get("filters", None))
    values.append((key, value.get("class"), value["universe"], filters_json))

# Insert data into the strategies table
cur.executemany(sql, values)


# Commit the transaction to save the changes
mydb.commit()

# Print number of rows inserted
print(cur.rowcount, "records inserted.")

# Close the cursor and connection
cur.close()
mydb.close()

def print_strategies(strategies):
    for name, details in strategies.items():
        print(f"Strategy Name: {name}")
        for key, value in details.items():
            print(f"  {key}: {value}")
        print()  # Add an empty line for better readability

# Call the function to print strategies
print_strategies(strategies)

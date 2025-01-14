import pandas as pd

def process_data(data):
    try:
        if isinstance(data, dict):
            # Create a DataFrame using Pandas
            df = pd.DataFrame(data)

            # Perform common data processing operations
            for column in df.columns:
                if pd.api.types.is_string_dtype(df[column]):
                    # Calculate word count for text columns
                    df[column + '_word_count'] = df[column].apply(lambda x: len(str(x).split()))

                    # Convert text to lowercase
                    df[column] = df[column].str.lower()

            # Additional processing logic based on your requirements
            # Example 1: Handling missing values by filling with a default value (e.g., "Not Available")
            df.fillna("Not Available", inplace=True)

            # Example 2: Remove duplicate rows based on all columns
            df.drop_duplicates(inplace=True)

            # Example 3: Apply a custom transformation
            df['example_column'] = df['example_column'].apply(lambda x: custom_transformation(x))

            # Additional transformation logic based on your requirements
            # Example 4: Replace specific values in a column
            df['another_column'] = df['another_column'].replace({'old_value1': 'new_value1', 'old_value2': 'new_value2'})

            # Example 5: Perform mathematical operations
            df['numeric_column'] = df['numeric_column'] * 2

            # Your additional processing logic here...
            # Replace the comments with the specific logic you need for your project

            # Return the processed data as a list of dictionaries
            processed_data = df.to_dict(orient='records')
            return processed_data

        else:
            return "Invalid data format for processing."

    except Exception as e:
        return f"Error: {str(e)}"

# Example custom transformation function
def custom_transformation(value):
    try:
        # Replace 'old_value' with your specific logic for transforming the value
        transformed_value = value.replace('old_value', 'new_value')

        # Additional transformation logic based on your requirements
        # For example, you might want to perform mathematical operations, handle special cases, etc.

        return transformed_value

    except Exception as e:
        return f"Transformation Error: {str(e)}"

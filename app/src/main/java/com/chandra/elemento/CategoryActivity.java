package com.chandra.elemento;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

public class CategoryActivity extends AppCompatActivity {

    Button maths;
    Button chem;
    Button phys;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_category);

        maths = (Button) findViewById(R.id.maths);
        chem = (Button) findViewById(R.id.chem);
        phys = (Button) findViewById(R.id.phy);

        maths.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(CategoryActivity.this, MathsActivity.class);
                startActivity(intent);
            }
        });

        chem.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(CategoryActivity.this, ChemistryActivity.class);
                startActivity(intent);
            }
        });

        phys.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(CategoryActivity.this, PhysicsActivity.class);
                startActivity(intent);
            }
        });
    }
}
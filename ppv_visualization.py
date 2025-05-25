import numpy as np
import matplotlib.pyplot as plt

def compute_ppv(sensitivity, specificity, prevalence):
    return (sensitivity * prevalence) / (sensitivity * prevalence + (1 - specificity) * (1 - prevalence))

sensitivity = 0.99
specificities = [0.99, 0.999, 0.9999, 0.99999]
prevalences = np.linspace(0.00001, 0.5, 500)

plt.figure()
for spec in specificities:
    ppv = compute_ppv(sensitivity, spec, prevalences)
    plt.plot(prevalences*100, ppv*100, label=f"Specificity {spec*100:.4f}%")
plt.xlabel("Prevalence (%)")
plt.ylabel("PPV (%)")
plt.title("PPV vs. Prevalence for Different Specificities (Sensitivity = 99%)")
plt.legend()
plt.tight_layout()
plt.savefig('ppv_plot.png')
plt.show()

# Integer checks
for prev_pct in [1, 5, 10, 50]:
    for spec_pct in [99, 99.9, 99.99, 99.999]:
        prev = prev_pct / 100
        spec = spec_pct / 100
        ppv_val = compute_ppv(sensitivity, spec, prev)
        print(f"Prevalence={prev_pct}%  Specificity={spec_pct}%  PPV={ppv_val*100:.1f}%")

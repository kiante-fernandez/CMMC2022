library(SimDesign)
library(here)
library(ggplot2)
# ### Define design conditions

Design <- createDesign(
  sample_size = c(5, 15),
  sig_squared = c(1, 4),
  groups_equal = c(TRUE, FALSE),
  distribution = c("GAUSS", "EXP", "UNI")
)
#condition <- Design[5,]
# #And then run
#Attach(condition)

#user_defined functions
get_exp_mean <- function(){}
get_uni_mean <- function(){}


#-------------------------------------------------------------------
### Define essential simulation functions
Generate <- function(condition, fixed_objects = NULL) {
  Attach(condition)
  
  if (groups_equal) {
    N1 <- N2 <- sample_size
    sd1 <- sd2 <- sig_squared
  } else {
    N1 <- sample_size
    N2 <- ifelse(N1 > 10, sample_size - 10, sample_size + 10)
    sd1 <- sig_squared
    sd2 <- ifelse(sd1 > 1, sig_squared - 3, sig_squared + 3)
  }
  dv <- switch(distribution,
               GAUSS = c(rnorm(N1, sd = sqrt(sd1)), rnorm(N2, sd = sqrt(sd2))),
               EXP = c(rexp(N1, rate = 1/sqrt(sd1) ), rexp(N2, rate = 1/ sqrt(sd2) )), # need correct values
               UNI = c(runif(N1, min = 0, max = 1), runif(N2, min = 0, max = 1)) # need correct values
  )
  dat <- data.frame(
    DV = dv,
    group = c(rep("G1", N1), rep("G2", N2))
  )
  dat
}

Analyse <- function(condition, dat, fixed_objects = NULL) {
  Attach(condition)
  Attach(dat)
  equal_variances <- TRUE
  # Run statistical analyses of interest ...
  test <- t.test(dat$DV[dat$group == "G1"], dat$DV[dat$group == "G2"],
                 var.equal = equal_variances
  )
  
  estimate_diff <- test$estimate[[1]] - test$estimate[[2]]
  
  p_value <- test$p.value[[1]]
  # Return a named vector or list
  ret <- c(estimate_diff = estimate_diff[[1]], p_value = p_value[[1]])
  ret
}

Summarise <- function(condition, results, fixed_objects = NULL) {
  Attach(condition)
  Attach(results)
  alpha_rate <- 0.05
  # Summarise the simulation results
  pwr <- EDR(p_value, alpha = alpha_rate)
  # Return a named vector of results
  ret <- c(
    pwr = pwr,
    mean_diff = colMeans(results)
  )
  ret
}

#-------------------------------------------------------------------
### Run the simulation
res <- runSimulation(
  design = Design, replications = 1000,
  generate = Generate,
  analyse = Analyse,
  summarise = Summarise,
  save_results = T,
  filename = paste0(
    "CMMC_t_test_",
    lubridate::today()
  ),
  parallel = T
  #boot_method = "basic"
)

res

# summary of simulation object
summary(res)
# print results
print(res)
names(res)

#TypeI <- subset(res, mean_diff.estimate_diff== 0)

ggplot(res, aes(sig_squared, pwr, colour = factor(sample_size))) +
  geom_point() +
  geom_line() +
  #geom_ribbon(aes(ymin = BOOT_pwr_2.5, ymax = BOOT_pwr_97.5, fill = factor(sample_size)), alpha = .3, linetype = 0) +
  xlab("sig_squared") +
  ylab("Detection Rate (Power)") +
  ggtitle("Empirical Power Curves with 95% CIs") +
  scale_fill_discrete("N") +
  scale_colour_discrete("N") +
  #geom_hline(yintercept = .80, linetype = "dashed", size = .3) +
  #geom_vline(xintercept = .3, linetype = "dashed", size = .3) +
  theme_classic()+
  facet_wrap(~distribution)

#another way to get the cases that might be of interest to try
Design <- createDesign(sample_size = list(c(5, 15),
                                          c(5,5),
                                          c(15,15)),
                       standard_deviations = list(c(1,4),
                                                  c(1,1),
                                                  c(4,4)),
                       dist = c("GAUSS", "EXP", "UNI"))
